import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_products_from_json(path="products.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            out = []
            for row in data:
                out.append({
                    "id": int(row.get("id")),
                    "name": str(row.get("name")),
                    "category": str(row.get("category")),
                    "price": float(row.get("price"))
                })
            return out
    except Exception:
        return []

def read_products_from_csv(path="products.csv"):
    out = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                out.append({
                    "id": int(row.get("id")),
                    "name": row.get("name"),
                    "category": row.get("category"),
                    "price": float(row.get("price"))
                })
    except Exception:
        out = []
    return out

def read_products_from_sqlite(path="products.db"):
    out = []
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for r in rows:
            out.append({
                "id": int(r[0]),
                "name": r[1],
                "category": r[2],
                "price": float(r[3])
            })
        conn.close()
    except Exception:
        out = []
    return out

@app.route("/products")
def products():
    source = request.args.get("source", "").lower()
    id_str = request.args.get("id")
    error = None
    products = []

    if source == "json":
        products = read_products_from_json()
    elif source == "csv":
        products = read_products_from_csv()
    elif source == "sql":
        products = read_products_from_sqlite()
    else:
        error = "Wrong source"

    if error is None and id_str is not None:
        try:
            target_id = int(id_str)
            products = [p for p in products if p["id"] == target_id]
            if len(products) == 0:
                error = None
        except Exception:
            products = []
            error = None

    return render_template("product_display.html", products=products, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

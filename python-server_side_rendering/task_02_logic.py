import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/items")
def show_items():
    items = []
    try:
        with open("items.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            raw = data.get("items", [])
            if isinstance(raw, list):
                items = raw
    except Exception:
        items = []

    return render_template("items.html", items=items)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

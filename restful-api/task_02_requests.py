#!/usr/bin/python3


import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        info = response.json()
        for i in info:
            print(i["title"])
    else:
        print("Request Failed.")

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        info = response.json()
        with open("posts.csv", "w") as f:
            rows = [{"id": i["id"], "title": i["title"], "body": i["body"]} for i in info]
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
    else:
        print("Request Failed.")

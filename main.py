from flask import Flask, jsonify, request
import csv

all_articles = []
liked_articles = []
not_liked_articles = []

file_pointer = open('articles.csv' , encoding = 'utf-8')
file_reader = csv.reader(file_pointer)
column_header = next(file_reader)
for article in file_reader:
    all_articles.append(article)
file_pointer.close()

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()
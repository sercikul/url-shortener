from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
import string 
from random import choices

# Initialise App
app = Flask(__name__)

# Create Database
client = PyMongo(app, uri="mongodb+srv://admin:mLrwHxBFZzA78TfX@urlshortener.rtjp9.mongodb.net/urls?retryWrites=true&w=majority")
db = client.db

# Encoding Algorithm
def url_shortener():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    while True:
        random_symbols = choices(chars, k=4)
        tag = "".join(random_symbols)
        encoded_url = "https://short.est/" + tag
        encoded = db.urls.find_one({"encoded": encoded_url})
        if not encoded:
            return encoded_url

# Landing page
@app.route('/')
def home():
    return render_template("home.html")

# Encode
@app.route('/encode', methods=["GET", "POST"])
def encode():
    if request.method == "POST":
        original_url = request.form["url"]
        retrieved_url = db.urls.find_one({"url": original_url})
        if retrieved_url:
            short_url = str(retrieved_url["encoded"])
            url = {"url": original_url, "encoded": short_url}
        else:
            short_url = url_shortener()
            db.urls.insert_one({"url": original_url, "encoded": short_url})
            url = {"url": original_url, "encoded": short_url}
        return jsonify(url)
    else:
        return render_template("encode.html")

# Decode
@app.route('/decode', methods=["GET", "POST"])
def decode():
    if request.method == "POST":
        short_url = request.form["url"]
        retrieved_short_url = db.urls.find_one({"encoded": short_url})
        if not retrieved_short_url:
            return "The entered short URL does not exist. Please try again !"
        else:
            original_url = str(retrieved_short_url["url"])
            url = {"url": original_url, "encoded": short_url}
            return jsonify(url)
    else:
        return render_template("decode.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
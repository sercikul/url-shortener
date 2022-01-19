from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
import string 
from random import choices

# Initialises Flask App 
app = Flask(__name__)

# MongoDB API 
client = PyMongo(app, uri="mongodb+srv://admin:mLrwHxBFZzA78TfX@urlshortener.rtjp9.mongodb.net/urls?retryWrites=true&w=majority")
db = client.db

def url_shortener():
    """ Encoding Algorithm: Randomly combines ASCII digits and lower-, 
    uppercase letters (k=4). Appends the combination as a tag to a fictional URL.  """
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    while True:
        random_symbols = choices(chars, k=4)
        tag = "".join(random_symbols)
        encoded_url = "https://short.est/" + tag
        encoded = db.urls.find_one({"encoded": encoded_url})
        if not encoded:
            return encoded_url

# Landing/Home Page 
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/encode', methods=["GET", "POST"])
def encode():
    """ Encode Page: Upon POST request, checks whether submitted URL already in database. 
    Otherwise, calls url_shortener() and stores the new short URL in MongoDB. """
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

@app.route('/decode', methods=["GET", "POST"])
def decode():
    """ Decode Page: Upon POST request, function checks whether submitted short URL
    in database. Otherwise, displays a corresponding message. """
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
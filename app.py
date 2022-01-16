from flask import Flask, render_template, request, redirect, url_for
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
        combo = "".join(random_symbols)
        encoded = db.urls.find_one({"encoded": combo})
        if not encoded:
            return combo

# Landing page - Encode
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        original_url = request.form["url"]
        retrieved_url = db.urls.find_one({"url": original_url})
        if not retrieved_url:
            short_url = url_shortener()
            db.urls.insert_one({"url": original_url, "encoded": short_url})
        else:
            short_url = retrieved_url["encoded"]
        return redirect(url_for("encode", short_url=short_url))
    else:
        return render_template("home.html")

# Landing page - Decode
@app.route('/home_dcd')
def home_decode():
    return render_template("decode.html")

# Displays encoded URL upon submission
@app.route('/encode/<short_url>')
def encode(short_url):
    return render_template("encode_result.html", short_url=short_url)

# Displays decoded URL upon submission
@app.route('/decode')
def decode():
    pass

if __name__ == '__main__':
    app.run(port=5000, debug=True)
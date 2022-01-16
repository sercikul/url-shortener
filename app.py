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
        tag = "".join(random_symbols)
        encoded_url = "https://short.est/" + tag
        encoded = db.urls.find_one({"encoded": encoded_url})
        if not encoded:
            return encoded_url

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
        short_tag = short_url[-4:]
        return redirect(url_for("encode", short_tag=short_tag))
    else:
        return render_template("home.html")

# Landing page - Decode
@app.route('/home_dcd', methods=["GET", "POST"])
def home_decode():
    if request.method == "POST":
        short_url = request.form["shorturl"]
        retrieved_short_url = db.urls.find_one({"encoded": short_url})
        if not retrieved_short_url:
            # Make error handling
            print("Error")
        else:
            short_tag = short_url[-4:]
        return redirect(url_for("decode", short_tag=short_tag))
    else:
        return render_template("decode.html")

# Displays encoded URL upon submission
@app.route('/encode/<short_tag>')
def encode(short_tag):
    return render_template("encode_result.html", short_tag=short_tag)

# Displays decoded URL upon submission
@app.route('/decode/<short_tag>')
def decode(short_tag):
    short_url = "https://short.est/" + short_tag
    retrieve_original = db.urls.find_one({"encoded": short_url})
    original_url = retrieve_original["url"]
    return render_template("decode_result.html", original_url=original_url)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
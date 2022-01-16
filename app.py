from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import string 
from random import choices

# Initialise App
app = Flask(__name__)

# Create Database

# Encoding Algorithm
def url_shortener():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    pass

# Landing page - Encode
@app.route('/', methods=["POST"])
def home():
    if request.method == "POST":
        original_url = request.form["url"]
        # Check if already in MongoDB database
        # else return short URL and store inside MongoDB
        if not original_url:
            short_url = url_shortener()
            # Insert to MongoDB
        else:
            # Retrieve 'short_url' from MongoDB
            pass

        return redirect(url_for("encode", short_url=short_url))
    else:
        return render_template("home.html")

# Landing page - Decode
@app.route('/home_dcd')
def home_decode():
    return render_template("decode.html")

# Displays encoded URL upon submission
@app.route('/encode')
def encode(short_url):
    return render_template("encode_result.html", short_url=short_url)

# Displays decoded URL upon submission
@app.route('/decode')
def decode():
    pass

if __name__ == '__main__':
    client = MongoClient("mongodb+srv://urlshortener.rtjp9.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority")
    db = client["url-database"]
    url = db["url"]
    encoded_url = db["encoded_url"]
    app.run(port=5000, debug=True)
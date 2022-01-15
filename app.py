from flask import Flask, render_template
from pymongo import MongoClient

# Initialise App
app = Flask(__name__)

# Landing page
@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
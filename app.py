from flask import Flask, render_template
from pymongo import MongoClient

# Initialise App
app = Flask(__name__)

# Landing page
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/home_dcd')
def home_decode():
    return render_template("decode.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
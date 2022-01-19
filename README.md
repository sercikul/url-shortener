# URL Shortener

The URL Shortener is a simple Flask (Python) web app. The web app encodes real URLs and shortens them. The user can also decode already shortened URLs back to their original version. URLs are stored in the database of a MongoDB Atlas cloud server.

## Installation

First, let us clone the repository. 
```bash
git clone https://github.com/sercikul/url-shortener.git
``` 
A virtual development environment, such as `venv`, is strongly recommended. Please install `venv`, if not already done.
```bash
pip install virtualenv
``` 
- Now, let us create a virtual environment called `venv`.
```bash
python -m venv venv
``` 
- Access your project folder and activate your virtual environment.
```bash
venv/Scripts/Activate.ps1
``` 

- Install the python dependencies on the virtual environment
```bash
pip install -r requirements.txt
```

- That's it! You can now start the web application. Have fun.
```python
python app.py
```

## Dependencies
```
certifi==2021.10.8
charset-normalizer==2.0.10
click==8.0.3
colorama==0.4.4
dnspython==2.1.0
Flask==2.0.2
Flask-PyMongo==2.3.0
idna==3.3
itsdangerous==2.0.1
Jinja2==3.0.3
MarkupSafe==2.0.1
pymongo==4.0.1
requests==2.27.1
urllib3==1.26.8
Werkzeug==2.0.2
```

## API Unit Testing
The `testing.py` file provides various API tests for the web app.

# Build API Project

This project builds an API to:
1. Create, delete and list comments/posts on a service (e.g facebook/reddit). The API also 
2. Counts the number of likes or dislikes on each post

The python Flask framework is used to build the REST API and can also be run inside Docker.. 

## Installation - Flask

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install flask
```

## Usage

```python
from flask import Flask

app = Flask(__name__)

# /status is the Resource, and methods 
# specifies the API method to use. Default is GET
@app.route('/status', methods=["POST"])

# to run the API from command line
user$ python3 -m flask run

```

## Installation - SQLite

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install sqlite
```

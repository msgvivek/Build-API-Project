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

## Usage

```python
# sqlite3 is an inbuilt package with python3
import sqlite3
```

## Installation - Docker

Go to docs.docker.com to install Docker for your PC

## Usage

1. Make a directory to store all scripts and files

2. Make a Dockerfile in the same directory

3. To run with the dockerfile:
```bash
docker build -t tag:tag .

docker run -ti tag:tag
```

4. To run with docker-compose.yaml
```bash
docker-compose up -d
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

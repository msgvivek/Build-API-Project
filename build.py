from flask import Flask
from flask import request
import build_data
import json

app = Flask(__name__)
conn = build_data.create_conn()

@app.route('/status', methods=["POST"])
def create():
    data = request.get_json()
    build_data.insert_values(conn, data)
    return data.get("status")

@app.route('/status')
def read():
    get_data = build_data.retrieve_values(conn)
    json_data = json.dumps(get_data)
    return json_data

@app.route('/status', methods=["PUT"])
def update():
    data = request.get_json()
    return json.dumps(build_data.update_values(conn, data))

@app.route('/status', methods=["DELETE"])
def delete():
    data = request.get_json()
    return json.dumps(build_data.delete_values(conn, data))

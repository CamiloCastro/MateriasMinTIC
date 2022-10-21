from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

def load_file_config():
  with open("config.json") as f:
    data = json.load(f)
  return data

@app.route("/suma", methods=["POST"])
def suma():
  jj = request.get_json()
  res = jj["n1"] + jj["n2"]
  data = { "result" : res }
  return jsonify(data)


@app.route("/post", methods=["POST"])
def test():
  data = { "message" : "The server is running (POST)...." }
  return jsonify(data)

@app.route("/put", methods=["PUT"])
def test1():
  data = { "message" : "The server is running (PUT)...." }
  return jsonify(data)

@app.route("/get", methods=["GET"])
def test2():
  data = { "message" : "The server is running (GET)...." }
  return jsonify(data)


if __name__ == "__main__":
  data_config = load_file_config()
  print(f"Server running : http://{data_config['url-backend']}:{data_config['port']}")
  serve(app, host=data_config["url-backend"], port=data_config["port"])
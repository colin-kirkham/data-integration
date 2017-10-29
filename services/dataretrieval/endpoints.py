from json import dumps

from mock import MockData
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello from the Data Service"

@app.route("/data/<customer_id>/<uuid>", methods=['GET'])
def retrieve(customer_id, uuid):
    data = MockData()
    response_data = data.retrieve(customer_id, uuid, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

if __name__ == "__main__":
    app.run(debug="True", port=5003)
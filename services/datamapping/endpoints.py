from json import dumps

from mock import MockMappings
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello from the Data Mapping Service"

@app.route("/mappings/<customer_id>", methods=['POST'])
def create(customer_id):
    mappings = MockMappings()
    response_data = mappings.create(customer_id, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

@app.route("/mappings/<customer_id>", methods=['GET'])
def retrieve(customer_id):
    mappings = MockMappings()
    response_data = mappings.retrieve(customer_id, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

@app.route("/mappings/<customer_id>/<uuid>", methods=['PUT'])
def update(customer_id, uuid):
    mappings = MockMappings()
    response_data = mappings.update(customer_id, uuid, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

@app.route("/mappings/<customer_id>/<uuid>", methods=['DELETE'])
def delete(customer_id, uuid):
    mappings = MockMappings()
    response_data = mappings.delete(customer_id, uuid, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "applications/json"
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5001)
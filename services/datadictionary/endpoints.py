from mock import MockDictionaries
from flask import Flask, request
from json import dumps

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello from the Data Dictionary Service"

@app.route("/dictionaries/<customer_id>", methods=['POST'])
def create(customer_id):
    dictionaries = MockDictionaries()
    response_data = dictionaries.create(customer_id, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

@app.route("/dictionaries/<customer_id>", methods=['GET'])
def retrieve(customer_id):
    dictionaries = MockDictionaries()
    response_data = dictionaries.retrieve(customer_id, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

@app.route("/dictionaries/<customer_id>/<uuid>", methods=['PUT'])
def update(customer_id, uuid):
    dictionaries = MockDictionaries()
    response_data = dictionaries.update(customer_id, uuid, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

@app.route("/dictionaries/<customer_id>/<uuid>", methods=['DELETE'])
def delete(customer_id, uuid):
    dictionaries = MockDictionaries()
    response_data = dictionaries.delete(customer_id, uuid, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

if __name__ == "__main__":
    app.run(debug="True", port=5002)
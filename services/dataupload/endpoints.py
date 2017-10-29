from json import dumps

# from dataupload import app
from mock import MockUploads
from uploads import Uploads
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello from the Data Upload Service"

@app.route("/uploads/<customer_id>", methods=['POST'])
def create(customer_id):
    uploads = Uploads()
    response_data = uploads.create(customer_id, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

@app.route("/uploads/<customer_id>", methods=['GET'])
def retrieve(customer_id):
    uploads = MockUploads()
    response_data = uploads.retrieve(customer_id, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

@app.route("/uploads/<customer_id>/<uuid>", methods=['PUT'])
def update(customer_id, uuid):
    uploads = MockUploads()
    response_data = uploads.update(customer_id, uuid, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

@app.route("/uploads/<customer_id>/<uuid>", methods=['DELETE'])
def delete_upload(customer_id, uuid):
    uploads = Uploads()
    response_data = uploads.delete(customer_id, uuid, request)
    response = app.make_response(dumps(response_data))
    response.mimetype = "application/json"
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5000)

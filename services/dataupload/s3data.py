import io
import uuid

import boto3

class S3DataSource:
    def __init__(self, identifier="", bucket="pb-data-integration", customer_id='xxxx'):
        self.bucket = bucket

        # Generate a random UUID to name a folder for isolation
        if identifier == "":
            self.uuid = str(uuid.uuid4())
        else:
            self.uuid = identifier

        self.customer_id = customer_id

        # Create a new folder based on the unique uuid inside the root directory
        self._create_directory()

    def upload_data(self, fileobj):
        # Upload a single xml data file to the directory named for the uuid generated or passed to
        # this object
        self._upload_fileobj(fileobj, "data.xml")

    def upload_schema(self, fileobj):
        # Upload a single xsd xml schema file to the directory named for the uuid generated or
        # passed to this object
        self._upload_fileobj(fileobj, "schema.xsd")

    def upload_name(self, name):
        # Upload a text file called name.txt containing the given name for the data set
        fileobj = io.BytesIO(name.encode())
        self._upload_fileobj(fileobj, "name.txt")

    def delete(self):
        # Delete the directory and it's contents
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('pb-data-integration')
        for obj in bucket.objects.filter(Prefix=self.customer_id + "/" + self.uuid + "/"):
            obj.delete()

    def _create_directory(self):
        s3 = boto3.client('s3')
        print("DEBUG: Trying to create {0} in bucket \"{1}\"".format(
            self.uuid + "/", self.bucket))
        s3.put_object(Bucket=self.bucket, Body="", Key=self.customer_id + "/" + self.uuid + "/")

    def _upload_fileobj(self, fileobj, filename):
        s3 = boto3.client('s3')
        s3.upload_fileobj(fileobj, self.bucket, self.customer_id + "/" + self.uuid + "/" + filename)

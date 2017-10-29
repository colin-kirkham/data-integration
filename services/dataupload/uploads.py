from s3data import S3DataSource
from humanize import naturalsize

class Uploads:
    def create(self, customer_id, request):
        result = {}
        folder = S3DataSource(customer_id=customer_id)
        data = request.files['data']
        result['data'] = self._fileobj_information(data)
        folder.upload_data(data)
        schema = request.files['schema']
        result['schema'] = self._fileobj_information(schema)
        folder.upload_schema(schema)
        result['id'] = folder.uuid
        result['customer_id'] = customer_id
        name = request.values['name']
        result['name'] = name
        folder.upload_name(name)
        result['message'] = 'Uploaded successfully'

        return result

    def retrieve(self, customer_id, request):
        return "I would have returned a set of records with this call."

    def update(self, customer_id, uuid, request):
        return "I would have updated the data with this call."

    def delete(self, customer_id, uuid, request):
        result = {}
        folder = S3DataSource(customer_id=customer_id, identifier=uuid)
        folder.delete()
        result['id'] = uuid
        result['customer_id'] = customer_id
        result['message'] = 'Deleted successfully'

        return result

    def _fileobj_information(self, fileobj):
        result = {}
        result['bytes'] = fileobj.seek(0, 2)
        result['readable'] = naturalsize(result['bytes'])
        fileobj.seek(0)

        return result

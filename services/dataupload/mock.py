import os
from random import randint
from uuid import uuid4

from humanize import naturalsize
from num2words import num2words


class MockUploads:

    def create(self, customer_id, request):
        result = {}
        data = request.files['data']
        result['data'] = self._fileobj_information(data)
        schema = request.files['schema']
        result['schema'] = self._fileobj_information(schema)
        result['id'] = str(uuid4())
        result['customer_id'] = customer_id
        name = request.values['name']
        result['name'] = name
        result['message'] = 'Uploaded successfully'

        return result

    def retrieve(self, customer_id, request):
        result = {}
        result['customer_id'] = customer_id
        result['uploads'] = [{'id': str(uuid4()), 'name': 'Dummy Name {}'
            .format(num2words(i+1).title())} for i in range(randint(1, 10))]

        return result

    def update(self, customer_id, uuid, request):
        result = {}
        data = request.files['data']
        result['data'] = self._fileobj_information(data)
        schema = request.files['schema']
        result['schema'] = self._fileobj_information(schema)
        result['id'] = uuid
        result['customer_id'] = customer_id
        name = request.values['name']
        result['name'] = name
        result['message'] = 'Updated successfully'

        return result

    def delete(self, customer_id, uuid, request):
        result = {}
        result['id'] = uuid
        result['customer_id'] = customer_id
        result['message'] = 'Deleted successfully'

        return result

    def _fileobj_information(self, fileobj):
        result = {}
        result['bytes'] = fileobj.seek(0, os.SEEK_END)
        result['readable'] = naturalsize(result['bytes'])

        return result

from uuid import uuid4
from num2words import num2words
from random import randint

class MockMappings:

    def create(self, customer_id, request):
        result = {}
        result['id'] = str(uuid4())
        result['customer_id'] = customer_id
        result['name'] = request.values['name']
        result['upload_id'] = request.values['upload_id']
        result['dictionary_id'] = request.values['dictionary_id']
        result['message'] = 'Created successfully'

        return result

    def retrieve(self, customer_id, request):
        result = {}
        result['customer_id'] = customer_id
        result['mappings'] = [{'id': str(uuid4()), 'name': "Mapping Name {}"
            .format(num2words(i+1).title()), 'upload_id': str(uuid4()), 
            'dictionary_id': str(uuid4())} for i in range(randint(1, 10))]

        return result

    def update(self, customer_id, uuid, request):
        result = {}
        result['id'] = uuid
        result['customer_id'] = customer_id
        result['name'] = request.values['name']
        result['upload_id'] = request.values['upload_id']
        result['dictionary_id'] = request.values['dictionary_id']
        result['message'] = 'Updated successfully'

        return result

    def delete(self, customer_id, uuid, request):
        result = {}
        result['id'] = uuid
        result['customer_id'] = customer_id
        result['message'] = 'Deleted successfully'

        return result
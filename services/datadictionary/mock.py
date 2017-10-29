from uuid import uuid4
from random import randint
from num2words import num2words

class MockDictionaries:

    def create(self, customer_id, request):
        result = {}
        result['id'] = str(uuid4())
        result['customer_id'] = customer_id
        result['name'] = request.values['name']
        result['definition'] = request.values['definition']
        result['message'] = 'Created successfully'

        return result

    def retrieve(self, customer_id, request):
        result = {}
        result['customer_id'] = customer_id
        result['dictionaries'] = [{'id': str(uuid4()), 'name': "Dictionary Name {}"
            .format(num2words(i+1).title()), 'definition': 'JSON Definition {}'.format(num2words(i+1).title()), 
            'dictionary_id': str(uuid4())} for i in range(randint(1, 10))]

        return result

    def update(self, customer_id, uuid, request):
        result = {}
        result['id'] = uuid
        result['customer_id'] = customer_id
        result['name'] = request.values['name']
        result['definition'] = request.values['definition']
        result['message'] = 'Updated successfully'

        return result

    def delete(self, customer_id, uuid, request):
        result = {}
        result['id'] = uuid
        result['customer_id'] = customer_id
        result['message'] = 'Deleted successfully'

        return result


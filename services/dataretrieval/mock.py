from names import get_first_name, get_last_name

class MockData:

    def retrieve(self, customer_id, uuid, request):
        result = {}
        # limit size start
        result['id'] = uuid
        result['customer_id'] = customer_id
        limit = int(request.values.get('limit', 10))
        result['limit'] = limit
        start = int(request.values.get('start', 0))
        result['start'] = start
        data = self._create_random_data(limit, start)
        result['data'] = data
        size = len(data)
        result['size'] = size

        return result

    def _create_random_data(self, limit, start):
        result = [{"id": i, "First Name": get_first_name(), "Last Name": get_last_name()} for i in range(start, limit + start)]
        return result

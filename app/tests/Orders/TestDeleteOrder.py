import uuid

from api_actions import create_order, delete_order
from common import BASE_URL, StatusCode
from models.order_input import OrderInput


class TestPlaceOrder:
    def setup_class(cls):
        cls.URL = BASE_URL + '/orders'

    def setup(self):
        self.order_data = OrderInput(stoks='EURUSD', quantity='0.11')
        _, response = create_order(self.order_data)
        self.order_id = response.get('id')

    def test_delete_order(self):
        code, response = delete_order(self.order_id)
        assert code == StatusCode.OK, "Unexpected HTTP code"
        assert not response

    def test_cannot_delete_nonexistent_order(self):
        code, _ = delete_order(uuid.uuid4())
        assert code == StatusCode.NOT_FOUND, "Unexpected HTTP code"

import uuid

from api_actions import create_order, get_order
from common import BASE_URL, StatusCode
from models.order_input import OrderInput


class TestGetOrder:
    def setup_class(cls):
        cls.URL = BASE_URL + '/orders'

    def setup(self):
        self.order_data = OrderInput(stoks='EURUSD', quantity='0.11')
        _, response = create_order(self.order_data)
        self.order_id = response.get('id')

    def test_get_order(self):
        code, response = get_order(self.order_id)
        assert code == StatusCode.OK, "Unexpected HTTP code"
        assert response.get('stoks') == self.order_data.stoks, \
            f"Stoks expected to be {self.order_data.stoks}, got {response.get('stoks')}"
        assert response.get('quantity') == self.order_data.quantity, \
            f"Quantity expected to be {self.order_data.quantity}, got {response.get('quantity')}"

    def test_cannot_get_nonexistent_order(self):
        code, _ = get_order(uuid.uuid4())
        assert code == StatusCode.NOT_FOUND, "Unexpected HTTP code"

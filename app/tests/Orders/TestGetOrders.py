from api_actions import create_order, get_all_orders
from common import BASE_URL, StatusCode
from models.order_input import OrderInput


class TestGetOrders:
    def setup_class(cls):
        cls.URL = BASE_URL + '/orders'

    def setup(self):
        self.order_ids = set()
        for _ in range(10):
            _, response = create_order(OrderInput(stoks='EURUSD', quantity='0.11'))
            self.order_ids.add(response.get('id'))

    def test_get_orders(self):
        code, response = get_all_orders()
        response_order_ids = (order.get('id') for order in response)
        assert code == StatusCode.OK, "Unexpected HTTP code"
        assert self.order_ids.issubset(response_order_ids), "Fetched orders dos not contain previously created ones"

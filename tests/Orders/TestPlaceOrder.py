import pytest
import requests

from api_actions import create_order
from common import BASE_URL, StatusCode
from models.order_input import OrderInput


class TestPlaceOrder:
    def setup_class(cls):
        cls.URL = BASE_URL + '/orders'

    @pytest.mark.parametrize(
        "stoks", ['', None, 'EURUSD', 'SOME_RANDOM_STRING']
    )
    @pytest.mark.parametrize(
        "quantity", [0, None, -0.01, 0.01, 1000000000, -100000000]
    )
    def test_order_creation(self, stoks, quantity):
        code, response_json = create_order(OrderInput(stoks=stoks, quantity=quantity))
        assert code == StatusCode.OK, "Unexpected HTTP code"
        assert response_json.get('stoks') == stoks, f"Stoks expected to be {stoks}, got {response_json.get('stoks')}"
        assert response_json.get('quantity') == quantity, \
            f"Quantity expected to be {quantity}, got {response_json.get('quantity')}"

    @pytest.mark.parametrize(
        "stoks", [1, True]
    )
    @pytest.mark.parametrize(
        "quantity", ['string', int(1), True]
    )
    def test_cannot_create_order_with_wrong_data_types(self, stoks, quantity):
        response = requests.post(BASE_URL+'/orders', data={"stoks":stoks, "quantity":quantity})
        assert response.status_code == StatusCode.UNPROCESSABLE_ENTITY, "Unexpected HTTP code"

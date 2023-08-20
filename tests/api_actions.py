import json
from uuid import UUID

import requests

from common import BASE_URL
from models.order_input import OrderInput


def create_order(order: OrderInput):
    response = requests.post(BASE_URL+'/orders', data=order.model_dump_json())
    return response.status_code, json.loads(response.text)


def get_all_orders():
    response = requests.get(BASE_URL + '/orders')
    return response.status_code, json.loads(response.text)


def get_order(order_id: UUID):
    response = requests.get(BASE_URL + '/orders' + f'/{order_id}')
    return response.status_code, json.loads(response.text)


def delete_order(order_id: UUID):
    response = requests.delete(BASE_URL + '/orders' + f'/{order_id}')
    return response.status_code, json.loads(response.text)

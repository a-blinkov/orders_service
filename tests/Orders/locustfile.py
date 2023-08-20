from locust import HttpUser, task

from models.order_input import OrderInput


class PlaceOrder(HttpUser):

    @task
    def place_order(self):
        self.client.post(url='/orders', data=OrderInput(stoks='EURUSD', quantity='0.11').model_dump_json())

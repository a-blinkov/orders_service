# trading_test_task
A RESTful API to simulate a Forex trading platform with WebSocket support for real-time order updates.

### Used tech:
Implemented async APIs for Orders read, creation, deletion using FastAPI. 

Models were generated with openapi-generator:

```npx @openapitools/openapi-generator-cli generate -i swagger.yaml -g python-fastapi -o <Project_Path>```

SqLite used for in-memory database, with one table "Orders".

For running the APIs used Uvicorn :

>[INFO] [Link to Uvicorn project page](https://www.uvicorn.org/)

```  uvicorn main:app --host 0.0.0.0 --port 8080 --reload ```

Automated tests wrote using pytest for parametrization and test run.


### How to deploy the service:
0. You need to have Docker be installed
   ([Link to how install Docker](https://docs.docker.com/engine/install/)) 
1. Clone the repository: 
    
    ```git clone https://github.com/a-blinkov/trading_test_task.git```
2. Go to the project folder:
    
    ```cd /<project directory>/trading_test_task/```
3. Execute docker compose up command in detached mode:
     
    ```docker compose up -d```
   
   It will build and run two docker containers:

   First with the service on ip 0.0.0.0:8080, second with the tests.

### How to run perf test:
install locust:

```pip install locust```

To run test for order creation run following command in console:

```locust -f <PATH_TO_THE_PROJECT>/trading_test_task/tests/Orders/locustfile.py --headless --users 100 --spawn 100 --host  http://0.0.0.0:8080 --run-time 5```

It will place 100 orders at second, during 5 seconds. After test finish you can see results at console.
#### Not implemented:
WebSocket functionality (would use [FastApi websocket](https://fastapi.tiangolo.com/advanced/websockets/))
   
Allure report generated, but couldn't be accessable from container (would use Jenkins for running tests in container, as [in my demo-project](https://github.com/a-blinkov/demo-jenkins))

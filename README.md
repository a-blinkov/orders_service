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
2. Go to the app folder:
    
    ```cd /<project directory>/trading_test_task/app```
3. Execute docker compose up command in detached mode:
     
    ```docker compose up -d```
   
   It will build and run two docker containers:

   First with the service on ip 0.0.0.0:8080, second with the tests.

#### Not implemented:
WebSocket functionality (would use [FastApi websocket](https://fastapi.tiangolo.com/advanced/websockets/))
   
Allure report generated, but couldn't be accessable from container (would use Jenkins for running tests in container, as [in my demo-project](https://github.com/a-blinkov/demo-jenkins))

Performance testing
[![PyPI version fury.io](https://badge.fury.io/py/kittymocklib-py.svg)](https://pypi.python.org/pypi/kittymocklib-py/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/kittymocklib-py.svg)](https://pypi.python.org/pypi/kittymocklib-py/)
[![GitHub tag](https://img.shields.io/github/tag/Suspir0n/kitty-Mock-Lib-Python.svg)](https://github.com/Suspir0n/kitty-Mock-Lib-Python/tags)


# kitty Mock Lib Python

A Python library for simulate an API with http and websocket request. In this `0.1.0.1` version of kitty-Mock-Lib-Python, allows you to simulate an API, being able to create routes in your own way, getting the history, details of it and other things you can do.

## Installation

The latest stable version [is available on PyPI](https://pypi.org/project/kittymocklib_py/). Either add `kittymocklib_py` to your `requirements.txt` file or install with pip:

    pip install kittymocklib-py

## Description

This project aims to help other types of projects that need a python API simulation and with this lib, you can simulate both http and websocket.

## Starting

To run the project, you will need to install the following programs:

- [Python: Required to create the project](https://www.python.org/downloads/)
- [Docker: Required to create the containers](https://www.docker.com/)
- [VS Code: For project development](https://code.visualstudio.com/)

## Steps

### Step 0:

In this lib we use a docker image from kitty Mock, so for you to use it you will have to create a `docker-compose.yml` file in order to take advantage of this lib:

    version: "3"
    services:
      kittymock1:
        image: ntopus/kitty-mock:0.4.5
        ports:
          - "6999:6999"
          - "7000-7020:7000-7020"
        environment:
          SERVER_PORT: 6999
          MOCKER_PORTS_RANGE: 7000-7020

In order to run the docker, first you have to `build` and then upload the container.

    docker-compose build 

Later:
    
    docker-compose up
Or can run this way:

    docker-compose up --build
              or
    docker-compose up --build -d

examples of how to use:

## How to use

### First steps

<details>
<summary>Http route</summary>
  
* Create the mocker

      from kittymocklib_py.mocker import Mocker

      def create_mocker():
          mocker = Mocker("http://localhost", 6999)
          print(f'My port: {mocker.mocker_port}')

* Create http mock route

      from kittymocklib_py.mocker import Mocker

      def create_http_mock_route():
          mocker = Mocker("http://localhost", 6999)
          route = mocker.create_http_route("/hello", "GET", 200, "hello my friend")

* Request http mock route

      from kittymocklib_py.mocker import Mocker

      def create_http_mock_route():
          mocker = Mocker("http://localhost", 6999)
          route = mocker.create_http_route("/hello", "GET", 200, "hello my friend")
          route_response = route.request()

* Delete mocker server

      from kittymocklib_py.mocker import Mocker

      def create_http_mock_route():
          mocker = Mocker("http://localhost", 6999)
          response = mocker.delete()

* Delete http mock route

      from kittymocklib_py.mocker import Mocker

      def create_http_mock_route():
          mocker = Mocker("http://localhost", 6999)
          route = mocker.create_http_route("/hello", "GET", 200, "hello my friend")
          route_response = route.delete()

* Get history http mock route

      from kittymocklib_py.mocker import Mocker

      def create_http_mock_route():
          mocker = Mocker("http://localhost", 6999)
          route = mocker.create_http_route("/hello", "GET", 200, "hello my friend")
          route_response = route.get_history()

* Clear history http mock route

      from kittymocklib_py.mocker import Mocker

      def create_http_mock_route():
          mocker = Mocker("http://localhost", 6999)
          route = mocker.create_http_route("/hello", "GET", 200, "hello my friend")
          route_response = route.clear_history()

* Details http mock route

      from kittymocklib_py.mocker import Mocker

      def create_http_mock_route():
          mocker = Mocker("http://localhost", 6999)
          route = mocker.create_http_route("/hello", "GET", 200, "hello my friend")
          route_response = route.details()
</details>

<details>
<summary>WebSocket</summary>

## Unavailable in this version

</details> 

## Test

In this lib, functional tests were used, with it we can run it like this:

    python -m unittest discover tests -v

## Additional

In this lib we use loggings, to be able to know everything that is going on behind the scenes, as well as to know if there was any error or bug somewhere in the code, it will demonstrate for you

## Configuration

To execute the project, it is necessary to use VsCode or an IDE of your preference, so that it identifies the dependencies necessary for execution in the repository. Once the project is imported, it will be possible to test its functionality in real time.

## Contributions

Contributions are always welcome! I hope I have helped someone in need.

## 🔓 License
MIT © [Evandro Silva](https://www.linkedin.com/in/suspir0n/)

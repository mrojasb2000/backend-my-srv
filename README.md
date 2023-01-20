# FastAPI

## Initial setup

1.- Check Python version

2.- Configure pyenv

3.- Install FastAPI framework

```sh
$ pip install "fastapi[all]"
```

## Usage

Running UVICORN server

```sh
$ uvicorn main:app --reload
```

where:

- main: file name
- app: module name

## Test API

- Using HTTP method "GET", path "/bar".

```sh
$ curl -X GET http://localhost:8000/bar
```

## Swagger Documentation

FastAPI Swagger automatic documentation

```sh
Open path "http://localhost:8000/docs" on your browser
```

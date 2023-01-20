from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World! from VIM"}


@app.get("/foo")
async def foo():
    return {"message": "bar"}

from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def get_root():
    return {"hello": "world"}

@app.get("/route-with-slash/")
def get_route_with_slash():
    return "slash"

@app.get("/route-with-no-slash")
def get_route_with_no_slash():
    return "no slash"

handler = Mangum(app, lifespan="off")
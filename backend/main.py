from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/hello-podman")
def hello_podman():
    array = np.array([1,2,3])
    print(array)
    return {"hello": "podman live"}
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def nain():
    return {'data':'OK'}
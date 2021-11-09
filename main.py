from fastapi import FastAPI
from settings import EXTERNAL_ENDPOINT


app = FastAPI()


@app.post(path="/analyse-string")
async def analyse_string():
    pass

from fastapi import FastAPI
from settings import EXTERNAL_ENDPOINT
from schemas import InAnalyseString

app = FastAPI()


@app.post(path="/analyse-string")
async def analyse_string(request: InAnalyseString):
    pass

from fastapi import FastAPI
from settings import EXTERNAL_ENDPOINT
from schemas import InAnalyseString
from utils import process_request

app = FastAPI()


@app.post(path="/analyse-string")
async def analyse_string(request: InAnalyseString):
    output_str = process_request(request)

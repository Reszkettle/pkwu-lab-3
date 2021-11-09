from schemas import InAnalyseString
import requests as req
from settings import EXTERNAL_ENDPOINT


def process_request(request: InAnalyseString) -> str:

    response = req.post(EXTERNAL_ENDPOINT, json={
        'string': request.string, 'substring': request.substring})
    if response.status_code == 200:
        pass

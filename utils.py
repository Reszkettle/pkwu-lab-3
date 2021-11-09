from schemas import InAnalyseString
import requests as req
from settings import EXTERNAL_ENDPOINT
from dicttoxml import dicttoxml
from fastapi import HTTPException


def csv_string_from_dict(data: dict) -> str:
    keys = [*data]
    values = [str(v) for v in data.values()]
    output_str = ','.join(keys)
    print(output_str)
    print(keys)
    print(values)
    output_str += '\n'
    output_str += ','.join(values)
    return output_str


def process_request(request: InAnalyseString) -> str:

    response = req.post(EXTERNAL_ENDPOINT, json={
        'string': request.string, 'substring': request.substring})
    if response.status_code == 200:
        data = response.json()
        if request.format == 'xml':
            return dicttoxml(data, custom_root='string-analyze-statistics', attr_type=False)
        elif request.format == 'csv':
            return csv_string_from_dict(data)
        return data

    raise HTTPException(
        status_code=502,
        detail="External API error"
    )

from schemas import InAnalyseString, Format
import requests as req
from settings import EXTERNAL_ENDPOINT
from dicttoxml import dicttoxml
from fastapi import HTTPException


def csv_string_from_dict(data: dict) -> str:
    keys = [*data]
    values = [str(v) for v in data.values()]
    output_str = ','.join(keys)
    output_str += '\n'
    output_str += ','.join(values)
    return output_str


def text_from_dict(data: dict) -> str:
    entries_str_list = []
    for key, value in data.items():
        entries_str_list.append(f"{key}: {value}")
    return ', '.join(entries_str_list)


def process_request(request: InAnalyseString) -> str:

    response = req.post(EXTERNAL_ENDPOINT, json={
        'string': request.string, 'substring': request.substring})
    if response.status_code == 200:
        data = response.json()
        if request.format == Format.XML:
            return dicttoxml(data, custom_root='string-analyze-statistics', attr_type=False)
        elif request.format == Format.CSV:
            return csv_string_from_dict(data)
        elif request.format == Format.TEXT:
            return text_from_dict(data)
        return data

    raise HTTPException(
        status_code=502,
        detail="External API error"
    )

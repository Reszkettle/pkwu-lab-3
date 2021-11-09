from pydantic import BaseModel
from typing import Optional
from enum import Enum


class Format(str, Enum):
    JSON = "json"
    XML = "xml"
    CSV = "csv"


class InAnalyseString(BaseModel):
    string: str
    substring: Optional[str] = None
    format: Format

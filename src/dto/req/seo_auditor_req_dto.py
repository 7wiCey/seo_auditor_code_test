from typing import Optional

from pydantic import BaseModel


class SeoAuditorRequestDto(BaseModel):
    url: str
    rules: list[str]

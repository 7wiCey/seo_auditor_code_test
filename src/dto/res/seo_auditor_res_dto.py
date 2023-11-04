from typing import Optional

from pydantic import BaseModel


class SeoAuditorResponseDto(BaseModel):
    condition_passed: bool
    failed_condition: Optional[list[str]] = None

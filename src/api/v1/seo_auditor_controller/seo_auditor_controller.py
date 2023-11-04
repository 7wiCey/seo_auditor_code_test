import json

from fastapi import HTTPException, Body
from starlette import status
from starlette.requests import Request

from src.api.v1 import router
from src.dto.req.seo_auditor_req_dto import SeoAuditorRequestDto
from src.dto.res.seo_auditor_res_dto import SeoAuditorResponseDto
from src.service.seo_auditor.seo_auditor_service import AuditorService

seo_service = AuditorService()


@router.post('/analysis', status_code=status.HTTP_200_OK,response_model=SeoAuditorResponseDto)
async def seo_analysis(req: SeoAuditorRequestDto):
    if not req.url or not req.rules:
        raise HTTPException(status_code=404, detail="Name field is required")
    seo_service.url = req.url
    seo_service.rules = req.rules
    return seo_service.analysis()
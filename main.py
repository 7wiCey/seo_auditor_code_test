# Since Replit doesn't import file well, so I have created a project and upload on it
# To make sure it works well, please download and run on local machine instead

from fastapi import FastAPI
from src.api.v1.seo_auditor_controller import seo_auditor_controller

app = FastAPI()


app.include_router(seo_auditor_controller.router)


# Default root endpoint
@app.get("/health-check")
async def root():
  return { "message": "The seo auditor is healthy"}


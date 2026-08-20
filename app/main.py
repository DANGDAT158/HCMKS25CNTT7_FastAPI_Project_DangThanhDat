from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.db.database import Base, engine
from app.models.user import User
from app.models.campaign import Campaign, CampaignMember
from app.models.campaign_task import CampaignTask


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="MARKETING CAMPAIGN MANAGEMENT API",
    version="1.0.0"
)

@app.exception_handler(HTTPException)
def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
            "data": None
        }
    )

@app.get("/health")
def health_check():
    return {
        "success": True,
        "message": "API is running",
        "data": {
            "status": "healthy"
        }
    }
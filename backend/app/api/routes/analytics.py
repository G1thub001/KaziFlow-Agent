from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.analytics import AnalyticsResponse

from app.services.analytics import analytics_service

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/",
    response_model=AnalyticsResponse,
)
def analytics(
    db: Session = Depends(get_db),
):

    return analytics_service.summary(db)
from fastapi import APIRouter
from app.schemas.health import Health

router = APIRouter()

@router.get("/health", response_model=Health)
def health_check():
    return Health(status="OK")

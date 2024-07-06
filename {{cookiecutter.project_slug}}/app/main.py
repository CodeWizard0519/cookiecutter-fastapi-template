from fastapi import FastAPI
from app.api.endpoints import health, predict
from app.core.config import settings

app = FastAPI(title=settings.project_name, version=settings.version)

app.include_router(health.router, prefix="/api/v1")
app.include_router(predict.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

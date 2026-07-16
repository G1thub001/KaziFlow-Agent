from fastapi import FastAPI

from app.api.routes.auth import router as auth_router
from app.core.config import settings

from app.models import User

from app.api.routes import auth
from app.api.routes import projects

app = FastAPI(
    title="KaziFlow Agent API"
)

app.include_router(auth.router)
app.include_router(projects.router)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "status": "running",
        "version": settings.APP_VERSION,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }
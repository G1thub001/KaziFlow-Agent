from fastapi import FastAPI

from app.core.config import settings

from app.api.routes.auth import router as auth_router
from app.api.routes.projects import router as project_router
from app.api.routes.workflows import router as workflow_router
from app.api.routes import agents

from app.api.routes.executions import router as execution_router

from app.api.routes.analytics import router as analytics_router



app = FastAPI(
    title="KaziFlow Agent API"
)

app.include_router(auth_router)
app.include_router(project_router)
app.include_router(workflow_router)
app.include_router(agents.router)
app.include_router(execution_router)
app.include_router(analytics_router)


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
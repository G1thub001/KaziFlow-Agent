from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.workflow import (
    WorkflowCreate,
    WorkflowResponse,
)
from app.services.workflow_service import (
    create_workflow,
    get_project_workflows,
)

router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"],
)


@router.post(
    "/{project_id}",
    response_model=WorkflowResponse,
)
def create(
    project_id: int,
    workflow: WorkflowCreate,
    db: Session = Depends(get_db),
):
    return create_workflow(
        db,
        workflow,
        project_id,
    )


@router.get(
    "/{project_id}",
    response_model=list[WorkflowResponse],
)
def list_workflows(
    project_id: int,
    db: Session = Depends(get_db),
):
    return get_project_workflows(
        db,
        project_id,
    )
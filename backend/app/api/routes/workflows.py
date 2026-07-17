from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException



from app.services.workflow_service import (
    run_workflow as run_workflow_service,
)
from app.auth.dependencies import get_current_user
from app.models.user import User


from app.database.dependencies import get_db
from app.schemas.workflow import (
    WorkflowCreate,
    WorkflowResponse,
    WorkflowRunRequest,
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

@router.post("/{workflow_id}/run")
def execute_workflow(
    workflow_id: int,
    request: WorkflowRunRequest,
    db: Session = Depends(get_db),
):
    result = run_workflow_service(
        db=db,
        workflow_id=workflow_id,
        user_input=request.user_input,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    return result
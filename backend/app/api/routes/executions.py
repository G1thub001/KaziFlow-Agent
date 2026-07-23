from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.execution import Execution
from app.schemas.execution import ExecutionResponse

router = APIRouter(
    prefix="/executions",
    tags=["Executions"],
)


@router.get(
    "/",
    response_model=list[ExecutionResponse],
)
def get_executions(
    db: Session = Depends(get_db),
):
    return db.query(Execution).all()


@router.get(
    "/workflow/{workflow_id}",
    response_model=list[ExecutionResponse],
)
def workflow_history(
    workflow_id: int,
    db: Session = Depends(get_db),
):
    return (
        db.query(Execution)
        .filter(
            Execution.workflow_id == workflow_id
        )
        .order_by(
            Execution.started_at
        )
        .all()
    )
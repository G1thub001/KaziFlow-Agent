from sqlalchemy.orm import Session

from app.models.workflow import Workflow
from app.schemas.workflow import WorkflowCreate


def create_workflow(
    db: Session,
    workflow: WorkflowCreate,
    project_id: int,
):
    db_workflow = Workflow(
        name=workflow.name,
        description=workflow.description,
        project_id=project_id,
    )

    db.add(db_workflow)
    db.commit()
    db.refresh(db_workflow)

    return db_workflow


def get_project_workflows(
    db: Session,
    project_id: int,
):
    return (
        db.query(Workflow)
        .filter(Workflow.project_id == project_id)
        .all()
    )
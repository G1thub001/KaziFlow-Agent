from sqlalchemy.orm import Session

from app.models.execution import Execution


class ExecutionCRUD:

    def create(
        self,
        db: Session,
        **kwargs,
    ):
        execution = Execution(**kwargs)

        db.add(execution)
        db.commit()
        db.refresh(execution)

        return execution

    def update(
        self,
        db: Session,
        execution: Execution,
        **kwargs,
    ):
        for key, value in kwargs.items():
            setattr(execution, key, value)

        db.commit()
        db.refresh(execution)

        return execution


execution_crud = ExecutionCRUD()
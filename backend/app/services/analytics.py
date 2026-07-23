from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.execution import Execution


class AnalyticsService:

    def summary(self, db: Session):

        total_executions = db.query(
            func.count(Execution.id)
        ).scalar()

        total_tokens = db.query(
            func.sum(Execution.total_tokens)
        ).scalar() or 0

        total_cost = db.query(
            func.sum(Execution.estimated_cost)
        ).scalar() or 0

        average_duration = db.query(
            func.avg(Execution.duration_ms)
        ).scalar() or 0

        return {
            "total_executions": total_executions,
            "total_tokens": total_tokens,
            "estimated_cost": round(total_cost, 6),
            "average_duration_ms": round(average_duration),

        }

    def workflow_history(
        self,
        db: Session,
        workflow_id: int,
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

analytics_service = AnalyticsService()
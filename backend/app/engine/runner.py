from app.engine.executor import AgentExecutor
from app.engine.context import ExecutionContext
from datetime import datetime


class WorkflowRunner:
    """
    Runs all agents belonging to a workflow.
    """

    def __init__(self):
        self.executor = AgentExecutor()

    def run(
        self,
        workflow,
        user_input,
    ):
        context = ExecutionContext(user_input)
        started_at = datetime.utcnow()
        execution_results = []

        for agent in workflow.agents:
            result = self.executor.execute(
                agent,
                context,
            )
            execution_results.append(result)

        completed_at = datetime.utcnow()
        duration_ms = int(
            (completed_at - started_at).total_seconds() * 1000
        )

        return {
            "workflow_id": workflow.id,
            "workflow_name": workflow.name,
            "status": "completed",

            "started_at": started_at.isoformat(),
            "completed_at": completed_at.isoformat(),
            "duration_ms": duration_ms,

            "agents_executed": len(execution_results),

            "results": execution_results,

            "context": context.outputs,
        }
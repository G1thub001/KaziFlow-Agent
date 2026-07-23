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

        print("=" * 60)
        print(f"Starting workflow: {workflow.name}")
        print("=" * 60)

        execution_results = []

        # Sort agents by execution order
        agents = sorted(
            workflow.agents,
            key=lambda agent: agent.execution_order,
        )

        # Execute each agent in order
        for agent in agents:
            # Skip inactive agents
            if not agent.is_active:
                print(f"Skipping {agent.name}")
                continue

            print("=" * 60)
            print(f"Executing [{agent.execution_order}] {agent.name}")

            result = self.executor.execute(
                agent,
                context,
            )
            execution_results.append(result)

            print(f"Completed {agent.name}")

        completed_at = datetime.utcnow()
        duration_ms = int(
            (completed_at - started_at).total_seconds() * 1000
        )

        print("=" * 60)
        print("Workflow complete.")
        print(f"Duration: {duration_ms} ms")
        print("=" * 60)


        total_tokens = sum(
            result.get("total_tokens", 0)
            for result in execution_results
        )

        total_duration = sum(
            result.get("duration_ms", 0)
            for result in execution_results
        )

        successful = sum(
            1
            for result in execution_results
            if result["status"] == "completed"
)

        failed = len(execution_results) - successful

        return {

            "workflow_id": workflow.id,

            "workflow_name": workflow.name,

            "status": "completed",

            "summary": {

                "agents": len(execution_results),

                "successful": successful,

                "failed": failed,

                "total_tokens": total_tokens,

                "total_duration_ms": total_duration,

            },

        "started_at": started_at.isoformat(),

        "completed_at": completed_at.isoformat(),

        "duration_ms": duration_ms,

        "results": execution_results,

        "context": context.history,
        }
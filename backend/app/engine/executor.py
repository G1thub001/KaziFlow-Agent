from datetime import datetime

from app.core.constants import DEFAULT_OUTPUT_FORMAT
from app.crud.execution import execution_crud
from app.database.session import SessionLocal
from app.prompts.builder import PromptBuilder
from app.providers.openrouter_provider import OpenRouterProvider
from app.services.pricing import pricing_service


class AgentExecutor:
    """
    Executes a single AI agent and records execution metadata.
    """

    def __init__(self):
        self.provider = OpenRouterProvider()

    def execute(self, agent, context):

        # -----------------------------
        # Build the system prompt
        # -----------------------------
        system_prompt = PromptBuilder(agent).build(
            user_request=context.user_request,
            shared_document=context.get_document(),
            document_version=context.get_version(),
            previous_agent=context.get_previous_agent(),
            knowledge=None,
            output_format=DEFAULT_OUTPUT_FORMAT,
        )

        db = SessionLocal()
        started_at = datetime.utcnow()

        try:
            # -----------------------------
            # Create execution record
            # -----------------------------
            execution = execution_crud.create(
                db=db,
                workflow_id=agent.workflow_id,
                agent_id=agent.id,
                status="running",
                provider=agent.provider,
                model=agent.model_name,
                started_at=started_at,
            )

            print(f"\nExecution #{execution.id} started")
            print(f"[{agent.execution_order}] {agent.name}")

            # -----------------------------
            # Run the AI model
            # -----------------------------
            response = self.provider.generate(
                system_prompt=system_prompt,
                user_prompt=context.user_request,
                temperature=agent.temperature,
                max_tokens=agent.max_tokens,
            )

            completed_at = datetime.utcnow()

            duration_ms = int(
                (completed_at - started_at).total_seconds() * 1000
            )

            # Calculate estimated cost using the pricing service
            estimated_cost = pricing_service.estimate_cost(
                model=response["model"],
                prompt_tokens=response["prompt_tokens"],
                completion_tokens=response["completion_tokens"],
            )

            # -----------------------------
            # Update execution record with token usage and actual model
            # -----------------------------
            execution_crud.update(
                db=db,
                execution=execution,
                status="completed",
                model=response["model"],  
                completed_at=completed_at,
                duration_ms=duration_ms,
                output=response["content"],
                prompt_tokens=response["prompt_tokens"],
                completion_tokens=response["completion_tokens"],
                total_tokens=response["total_tokens"],
                estimated_cost=estimated_cost,
            )

            print(
                f"[{agent.execution_order}] "
                f"{agent.name} completed "
                f"({duration_ms} ms, {response['total_tokens']} tokens, "
                f"${estimated_cost:.6f})"
            )

            # -----------------------------
            # Update shared document
            # -----------------------------
            context.update_document(
                agent_name=agent.name,
                role=agent.role or "Unknown",
                execution_order=agent.execution_order,
                output=response["content"],
            )

            return {
                "agent_id": agent.id,
                "agent_name": agent.name,
                "agent_type": agent.agent_type,
                "provider": agent.provider,
                "model": response["model"],  
                "status": "completed",
                "duration_ms": duration_ms,
                "output": response["content"],
                "prompt_tokens": response["prompt_tokens"],
                "completion_tokens": response["completion_tokens"],
                "total_tokens": response["total_tokens"],
                "estimated_cost": estimated_cost,
            }

        except Exception as e:
            # Update execution record with failure status
            execution_crud.update(
                db=db,
                execution=execution,
                status="failed",
                completed_at=datetime.utcnow(),
                error_message=str(e),
            )

            # Improved failure log with error details
            print(
                f"[{agent.execution_order}] "
                f"{agent.name} FAILED: {e}"
            )

            raise

        finally:
            db.close()
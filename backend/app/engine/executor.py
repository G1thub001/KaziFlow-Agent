from app.providers.openrouter_provider import OpenRouterProvider
from app.prompts.builder import PromptBuilder

from app.core.constants import DEFAULT_OUTPUT_FORMAT

class AgentExecutor:
    """
    Executes a single agent.
    Later this class will call OpenAI, Ollama, Claude, etc.
    """

    def __init__(self):
        self.provider = OpenRouterProvider()

    def execute(self, agent, context):
        # Build the prompt using PromptBuilder with workflow state
        system_prompt = PromptBuilder(agent).build(
            user_request=context.user_request,
            shared_document=context.get_document(),
            document_version=context.get_version(),
            previous_agent=context.get_previous_agent(),
            knowledge=None,
            output_format=DEFAULT_OUTPUT_FORMAT,
        )

        # The user prompt is ALWAYS the original user request
        # The shared document evolves in the system prompt
        output = self.provider.generate(
            system_prompt=system_prompt,
            user_prompt=context.user_request,
            temperature=agent.temperature,
            max_tokens=agent.max_tokens,
        )

        # Update the shared document with the agent's contribution
        context.update_document(
            agent_name=agent.name,
            role=agent.role or "Unknown",
            execution_order=agent.execution_order,
            output=output,
        )

        return {
            "agent_id": agent.id,
            "agent_name": agent.name,
            "agent_type": agent.agent_type,
            "provider": agent.provider,
            "status": "completed",
            "output": output,
        }
from app.providers.openrouter_provider import OpenRouterProvider
from app.prompts.builder import PromptBuilder

class AgentExecutor:
    """
    Executes a single agent.
    Later this class will call OpenAI, Ollama, Claude, etc.
    """

    def __init__(self):
        self.provider = OpenRouterProvider()

    def execute(self, agent, context):
        system_prompt = PromptBuilder(agent).build()

        output = self.provider.generate(
            system_prompt=system_prompt,
            user_prompt=context.current_message,
        )

        context.add_output(
            agent.name,
            output,
        )

        return {
            "agent_id": agent.id,
            "agent_name": agent.name,
            "agent_type": agent.agent_type,
            "provider": agent.provider,
            "status": "completed",
            "output": output,
        }
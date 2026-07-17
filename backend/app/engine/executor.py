class AgentExecutor:
    """
    Executes a single agent.
    Later this class will call OpenAI, Ollama, Claude, etc.
    """

    def execute(self, agent, context):
        output = (
            f"{agent.name} processed:\n"
            f"{context.current_message}"
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
class PromptBuilder:
    """
    Builds prompts for AI agents.
    """

    def __init__(self, agent):
        self.agent = agent

    def build(self) -> str:
        return f"""
You are {self.agent.name}.

Agent Type:
{self.agent.agent_type}

Your task is to assist as part of a workflow.

Be professional, concise, and accurate.
"""
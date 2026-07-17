class ExecutionContext:
    """
    Shared state passed between agents during workflow execution.
    """

    def __init__(self, user_input: str):
        self.user_input = user_input

        # The message the next agent will process
        self.current_message = user_input

        # History of every execution
        self.outputs = []

    def add_output(self, agent_name: str, output: str):
        self.outputs.append(
            {
                "agent": agent_name,
                "output": output,
            }
        )

        # Pass this output to the next agent
        self.current_message = output
from datetime import datetime


class ExecutionContext:
    """
    Shared workflow state passed between all agents.
    """

    def __init__(self, user_request: str):

        # Original user request (never changes)
        self.user_request = user_request

        # Current collaborative document
        self.current_document = ""

        # Document version
        self.document_version = 0

        # Previous contributor
        self.previous_agent = None

        # Execution history
        self.history = []

    def update_document(
        self,
        agent_name: str,
        role: str,
        execution_order: int,
        output: str,
    ):

        # Update current document
        self.current_document = output

        # Increment version
        self.document_version += 1

        # Remember who edited last
        self.previous_agent = agent_name

        # Record history
        self.history.append(
            {
                "version": self.document_version,
                "execution_order": execution_order,
                "agent": agent_name,
                "role": role,
                "timestamp": datetime.utcnow().isoformat(),
                "output": output,
            }
        )

    def get_document(self):
        return self.current_document

    def get_version(self):
        return self.document_version

    def get_previous_agent(self):
        return self.previous_agent
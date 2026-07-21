from pydantic import BaseModel


class AgentCreate(BaseModel):
    name: str
    agent_type: str
    provider: str
    model_name: str
    role: str
    goal: str
    instructions: str | None = None


class AgentResponse(BaseModel):
    id: int
    name: str
    agent_type: str
    provider: str
    model_name: str
    workflow_id: int

    model_config = {
        "from_attributes": True
    }
from pydantic import BaseModel


class AgentCreate(BaseModel):
    name: str
    agent_type: str
    provider: str
    model_name: str


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
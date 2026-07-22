from pydantic import BaseModel


class AgentCreate(BaseModel):
    name: str
    agent_type: str
    provider: str
    model_name: str
    workflow_id: int

    role: str | None = None
    goal: str | None = None
    instructions: str | None = None
    backstory: str | None = None

    temperature: float = 0.7
    max_tokens: int = 1000
    is_active: bool = True

    execution_order: int = 1

class AgentUpdate(BaseModel):
    name: str | None = None
    agent_type: str | None = None
    provider: str | None = None
    model_name: str | None = None

    role: str | None = None
    goal: str | None = None
    instructions: str | None = None
    backstory: str | None = None

    temperature: float | None = None
    max_tokens: int | None = None
    is_active: bool | None = None 

    execution_order: int | None = None  


class AgentResponse(BaseModel):
    id: int
    name: str
    agent_type: str
    provider: str
    model_name: str
    workflow_id: int

    role: str | None

    goal: str | None

    backstory: str | None

    temperature: float

    max_tokens: int

    is_active: bool

    execution_order: int

    model_config = {
        "from_attributes": True
    }
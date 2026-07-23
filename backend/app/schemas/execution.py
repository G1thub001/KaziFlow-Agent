from datetime import datetime

from pydantic import BaseModel


class ExecutionResponse(BaseModel):
    id: int

    workflow_id: int

    agent_id: int

    status: str

    provider: str

    model: str

    started_at: datetime

    completed_at: datetime | None

    duration_ms: int | None

    prompt_tokens: int

    completion_tokens: int

    total_tokens: int

    estimated_cost: float

    output: str | None

    error_message: str | None

    model_config = {
        "from_attributes": True
    }
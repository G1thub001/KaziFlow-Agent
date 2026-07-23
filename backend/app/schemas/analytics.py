from pydantic import BaseModel


class AnalyticsResponse(BaseModel):

    total_executions: int

    total_tokens: int

    estimated_cost: float

    average_duration_ms: int
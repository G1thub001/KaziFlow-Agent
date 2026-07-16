from pydantic import BaseModel


class WorkflowBase(BaseModel):
    name: str
    description: str | None = None


class WorkflowCreate(WorkflowBase):
    pass


class WorkflowResponse(WorkflowBase):
    id: int
    status: str
    project_id: int

    class Config:
        from_attributes = True
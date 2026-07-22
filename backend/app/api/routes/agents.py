from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.agent import (
    AgentCreate,
    AgentUpdate,
    AgentResponse,
)

from app.services.agent_service import (
    create_agent,
    get_workflow_agents,
    update_agent,
)

router = APIRouter(
    prefix="/agents",
    tags=["Agents"],
)


@router.post(
    "/{workflow_id}",
    response_model=AgentResponse,
)
def create_new_agent(
    workflow_id: int,
    agent: AgentCreate,
    db: Session = Depends(get_db),
):
    return create_agent(
        db,
        workflow_id,
        agent,
    )


@router.get(
    "/{workflow_id}",
    response_model=list[AgentResponse],
)
def list_agents(
    workflow_id: int,
    db: Session = Depends(get_db),
):
    return get_workflow_agents(
        db,
        workflow_id,
    )

@router.patch(
    "/{agent_id}",
    response_model=AgentResponse,
)
def update(
    agent_id: int,
    updates: AgentUpdate,
    db: Session = Depends(get_db),
):
    agent = update_agent(
        db,
        agent_id,
        updates,
    )

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent not found",
        )

    return agent


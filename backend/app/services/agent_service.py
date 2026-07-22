from sqlalchemy.orm import Session

from app.models.agent import Agent
from app.schemas.agent import (
    AgentCreate,
    AgentUpdate,
)


def create_agent(
    db: Session,
    workflow_id: int,
    agent: AgentCreate,
    
):
    db_agent = Agent(
        name=agent.name,
        agent_type=agent.agent_type,
        provider=agent.provider,
        model_name=agent.model_name,
        workflow_id=workflow_id,
        role=agent.role,
        goal=agent.goal,
        backstory=agent.backstory,
        temperature=agent.temperature,
        max_tokens=agent.max_tokens,
        is_active=agent.is_active,
    )

    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)

    return db_agent


def get_workflow_agents(
    db: Session,
    workflow_id: int,
):
    return (
        db.query(Agent)
        .filter(Agent.workflow_id == workflow_id)
        .all()
    )

def update_agent(
    db: Session,
    agent_id: int,
    updates: AgentUpdate,
):
    agent = db.get(Agent, agent_id)

    if not agent:
        return None

    update_data = updates.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(agent, field, value)

    db.commit()
    db.refresh(agent)

    return agent
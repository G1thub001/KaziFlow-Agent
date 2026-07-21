from sqlalchemy.orm import Session

from app.models.agent import Agent
from app.schemas.agent import AgentCreate


def create_agent(
    db: Session,
    workflow_id: int,
    agent: AgentCreate,
):
    db_agent = Agent(
        name=agent.name,
        role=agent.role,
        goal=agent.goal,
        instructions=agent.instructions,
        agent_type=agent.agent_type,
        provider=agent.provider,
        workflow_id=workflow_id,
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
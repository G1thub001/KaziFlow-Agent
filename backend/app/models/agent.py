from sqlalchemy import (
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Agent(Base):
    __tablename__ = "agents"

    # === Core Fields ===
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    agent_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    provider: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    model_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    workflow_id: Mapped[int] = mapped_column(
        ForeignKey("workflows.id"),
        nullable=False,
    )

    execution_order: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    # === Relationships ===
    workflow = relationship(
        "Workflow",
        back_populates="agents",
    )

    executions = relationship(
        "Execution",
        back_populates="agent",
    )

    # === Agent Intelligence Configuration ===
    role: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    goal: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    instructions: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    backstory: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    temperature: Mapped[float] = mapped_column(
        Float,
        default=0.7,
    )

    max_tokens: Mapped[int] = mapped_column(
        Integer,
        default=1000,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    def __repr__(self) -> str:
        return f"<Agent(id={self.id}, name='{self.name}', agent_type='{self.agent_type}')>"
from sqlalchemy import Integer, String, ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Agent(Base):
    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255)
    )

    agent_type: Mapped[str] = mapped_column(
        String(100)
    )

    provider: Mapped[str] = mapped_column(
        String(100)
    )

    model_name: Mapped[str] = mapped_column(
        String(100)
    )

    workflow_id: Mapped[int] = mapped_column(
        ForeignKey("workflows.id")
    )

    workflow = relationship(
        "Workflow",
        back_populates="agents",
    )

    role: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    goal: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    instructions: Mapped[str] = mapped_column(
        String(2000),
        nullable=True,
    )
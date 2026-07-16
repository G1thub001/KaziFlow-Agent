from sqlalchemy import String, Integer, ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Workflow(Base):
    __tablename__ = "workflows"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255)
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="draft",
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id")
    )

    project = relationship(
        "Project",
        back_populates="workflows",
    )

    agents = relationship(
    "Agent",
    back_populates="workflow",
    cascade="all, delete-orphan",
)
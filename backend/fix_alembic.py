from sqlalchemy import create_engine, text
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

with engine.begin() as conn:
    conn.execute(
        text(
            """
            UPDATE alembic_version
            SET version_num = '796871a99d87'
            """
        )
    )

print("Alembic version updated successfully!")
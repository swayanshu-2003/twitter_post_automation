from logging.config import fileConfig
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # adds project root to path

from app.config import DB_URL  # your actual DB URL
from app.db.models import Base  # Import Base if models are defined here

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

config = context.config

# Inject your actual DB URL into alembic config
config.set_main_option("sqlalchemy.url", DB_URL)

# Logging setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Provide target metadata for autogeneration
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    context.configure(
        url=DB_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

import os
from dotenv import load_dotenv
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context

# Carrega as variáveis de ambiente
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Importa o Base do models.py
from models import Base

# Configura os metadados corretamente
target_metadata = Base.metadata

# Configuração do Alembic
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

def run_migrations_offline():
    """Executa migrações no modo offline."""
    context.configure(url=DATABASE_URL, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Executa migrações no modo online."""
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

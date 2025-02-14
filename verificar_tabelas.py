from sqlalchemy import create_engine, inspect
import os

# Carregue a URL do banco de dados a partir da variável de ambiente
DATABASE_URL = os.getenv("DATABASE_URL")

# Crie o engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crie um inspetor de banco de dados
inspector = inspect(engine)

# Liste as tabelas no banco de dados
tabelas = inspector.get_table_names()
print("Tabelas no banco de dados:", tabelas)

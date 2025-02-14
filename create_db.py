from db import engine, Base  # Certifique-se de que esse import está correto
from models import Empresa, ObrigacaoAcessoria  # Importando os modelos

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")

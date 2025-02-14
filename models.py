from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Date

# Criação do Base diretamente aqui
Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    endereco = Column(String)
    email = Column(String)
    telefone = Column(String)

    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")

class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    periodicidade = Column(String)  # Pode ser mensal, trimestral, anual
    empresa_id = Column(Integer, ForeignKey('empresas.id'))

    empresa = relationship("Empresa", back_populates="obrigacoes")

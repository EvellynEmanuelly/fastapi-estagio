import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Empresa, ObrigacaoAcessoria, Base
from fastapi import FastAPI

# Criação da aplicação FastAPI
app = FastAPI()

# Conexão com o banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criando as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Schemas Pydantic
class EmpresaCreate(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class ObrigacaoAcessoriaCreate(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

# Endpoints para Empresa

@app.post("/empresas/")
def create_empresa(empresa: EmpresaCreate):
    db = SessionLocal()
    db_empresa = Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    db.close()
    return db_empresa

@app.get("/empresas/")
def get_empresas():
    db = SessionLocal()
    empresas = db.query(Empresa).all()
    db.close()
    return empresas

@app.get("/empresas/{empresa_id}")
def get_empresa(empresa_id: int):
    db = SessionLocal()
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    db.close()
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

@app.put("/empresas/{empresa_id}")
def update_empresa(empresa_id: int, empresa: EmpresaCreate):
    db = SessionLocal()
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if not db_empresa:
        db.close()
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    for key, value in empresa.dict().items():
        setattr(db_empresa, key, value)
    db.commit()
    db.refresh(db_empresa)
    db.close()
    return db_empresa

@app.delete("/empresas/{empresa_id}")
def delete_empresa(empresa_id: int):
    db = SessionLocal()
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if not db_empresa:
        db.close()
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    db.delete(db_empresa)
    db.commit()
    db.close()
    return {"message": "Empresa excluída com sucesso"}

# Endpoints para Obrigação Acessória
@app.post("/obrigacoes/")
def create_obrigacao(obrigacao: ObrigacaoAcessoriaCreate):
    db = SessionLocal()
    empresa = db.query(Empresa).filter(Empresa.id == obrigacao.empresa_id).first()
    if not empresa:
        db.close()
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    db_obrigacao = ObrigacaoAcessoria(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    db.close()
    return db_obrigacao

@app.get("/obrigacoes/")
def get_obrigacoes():
    db = SessionLocal()
    obrigacoes = db.query(ObrigacaoAcessoria).all()
    db.close()
    return obrigacoes
    
@app.get("/obrigacoes/{obrigacao_id}")
def get_obrigacao(obrigacao_id: int):
    db = SessionLocal()
    obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    db.close()
    
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação Acessória não encontrada")
    
    return obrigacao

@app.put("/obrigacoes/{obrigacao_id}")
def update_obrigacao(obrigacao_id: int, obrigacao: ObrigacaoAcessoriaCreate):
    db = SessionLocal()
    db_obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    if not db_obrigacao:
        db.close()
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    for key, value in obrigacao.dict().items():
        setattr(db_obrigacao, key, value)
    db.commit()
    db.refresh(db_obrigacao)
    db.close()
    return db_obrigacao

@app.delete("/obrigacoes/{obrigacao_id}")
def delete_obrigacao(obrigacao_id: int):
    db = SessionLocal()
    db_obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    if not db_obrigacao:
        db.close()
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    db.delete(db_obrigacao)
    db.commit()
    db.close()
    return {"message": "Obrigação excluída com sucesso"}

@app.get("/empresas/{empresa_id}")
def get_empresa(empresa_id: int):
    db = SessionLocal()
    empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    db.close()
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

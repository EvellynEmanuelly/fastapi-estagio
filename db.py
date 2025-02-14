import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Empresa, ObrigacaoAcessoria

app = FastAPI()

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
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresas/")
def get_empresas(db: Session = Depends(get_db)):
    empresas = db.query(Empresa).all()
    return empresas

@app.put("/empresas/{empresa_id}")
def update_empresa(empresa_id: int, empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    for key, value in empresa.dict().items():
        setattr(db_empresa, key, value)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.delete("/empresas/{empresa_id}")
def delete_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if not db_empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    db.delete(db_empresa)
    db.commit()
    return {"message": "Empresa excluída com sucesso"}

# Endpoints para Obrigação Acessória
@app.post("/obrigacoes/")
def create_obrigacao(obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    empresa = db.query(Empresa).filter(Empresa.id == obrigacao.empresa_id).first()
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    db_obrigacao = ObrigacaoAcessoria(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.get("/obrigacoes/")
def get_obrigacoes(db: Session = Depends(get_db)):
    obrigacoes = db.query(ObrigacaoAcessoria).all()
    return obrigacoes

@app.put("/obrigacoes/{obrigacao_id}")
def update_obrigacao(obrigacao_id: int, obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    for key, value in obrigacao.dict().items():
        setattr(db_obrigacao, key, value)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.delete("/obrigacoes/{obrigacao_id}")
def delete_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    db.delete(db_obrigacao)
    db.commit()
    return {"message": "Obrigação excluída com sucesso"}

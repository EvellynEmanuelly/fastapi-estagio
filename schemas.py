from pydantic import BaseModel, Field
import re

class EmpresaCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100, description="Nome da empresa deve ter entre 3 e 100 caracteres.")
    cnpj: str = Field(..., regex=r'^\d{14}$', description="CNPJ deve conter exatamente 14 dígitos numéricos.")
    endereco: str = Field(..., min_length=5, max_length=255, description="Endereço deve ter entre 5 e 255 caracteres.")
    email: str = Field(..., description="Email deve ser válido.")

    @classmethod
    def validate_cnpj(cls, cnpj: str) -> str:
        """Validação adicional para garantir que o CNPJ tem apenas números."""
        if not re.fullmatch(r"\d{14}", cnpj):
            raise ValueError("CNPJ deve conter exatamente 14 dígitos numéricos.")
        return cnpj

    @classmethod
    def validate_email(cls, email: str) -> str:
        """Validação básica de email."""
        if "@" not in email or "." not in email:
            raise ValueError("O email informado não é válido.")
        return email

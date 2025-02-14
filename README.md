# **FastApi-Estágio**  

## **API de Cadastro de Empresas e Obrigações Acessórias**  

### **Visão Geral**  
Este projeto consiste em uma API desenvolvida com FastAPI, que permite o cadastro e gerenciamento de empresas e suas obrigações acessórias. A API foi construída para ser simples de configurar e fácil de integrar a outros sistemas.  

---

## **Ferramentas e Tecnologias**  
- **Linguagem:** Python 3.7+  
- **Framework:** FastAPI  
- **Validação de Dados:** Pydantic  
- **Banco de Dados:** SQLite (pode ser substituído por PostgreSQL ou MySQL)  
- **ORM:** SQLAlchemy  
- **Servidor:** Uvicorn  
- **Gerenciamento de Código:** GitHub  
- **Editor Recomendado:** VS Code  
- **Testes de API:** Postman ou Insomnia  

---

## **Configuração do Ambiente**  

### **1. Instalar o Python**  
Baixe e instale a versão mais recente do Python (3.7 ou superior) em:  
🔗 [python.org/downloads](https://www.python.org/downloads/)  

Verifique a instalação executando:  
`python --version`  

### **2. Criar e Ativar o Ambiente Virtual**  
No terminal, dentro do diretório do projeto, execute:  
`python -m venv venv`  

Ative o ambiente virtual:  
- **Windows:** `venv\Scripts\activate`  
- **Linux/Mac:** `source venv/bin/activate`  

### **3. Instalar Dependências**  
Instale todas as bibliotecas necessárias com:  
`pip install -r requirements.txt`  

### **4. Rodar o Servidor**  
Inicie a API executando:  
`uvicorn main:app --reload`  

A API ficará disponível em: **http://127.0.0.1:8000**  

### **5. Acessar a Documentação**  
- **Swagger UI:** http://127.0.0.1:8000/docs  
- **Redoc:** http://127.0.0.1:8000/redoc  

---

## **Endpoints da API**  

### **📌 /companies/**  
- **GET** ➝ Buscar por todas as empresas  
- **POST** ➝ Criar uma nova empresa
- **GET /{id}** ➝ Buscar empresa por ID  
- **PUT /{id}** ➝ Atualizar empresa por ID  
- **DELETE /{id}** ➝ Excluir empresa por ID

### **📌 /obrigacoes/**  
- **GET** ➝ Buscar por todas as obrigações acessórias
- **POST** ➝ Criar uma nova obrigação acessória
- **GET /{id}** ➝ Buscar por ID  
- **PUT /{id}** ➝ Atualizar obrigação acessória  
- **DELETE /{id}** ➝ Excluir obrigação acessória  

---

## **Licença**  
📌 Direitos Reservados - Este projeto é de uso restrito e não pode ser copiado, distribuído ou publicado sem autorização.  
🚫 Proibida a reprodução total ou parcial sem permissão.  

📌 **Desenvolvido por:** Evellyn Emanuelly  

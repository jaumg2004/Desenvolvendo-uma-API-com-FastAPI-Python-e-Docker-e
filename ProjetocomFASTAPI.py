from fastapi import FastAPI, Query, HTTPException
from fastapi_pagination import Page, paginate
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

app = FastAPI()

# Modelo Pydantic para a resposta dos atletas
class AtletaResponse(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str

# Exemplo de banco de dados simulado
db = []

# Endpoint para buscar atletas com query parameters
@app.get("/atletas/")
async def get_atletas(nome: str = None, cpf: str = None):
    if nome:
        return [atleta for atleta in db if atleta['nome'] == nome]
    elif cpf:
        return [atleta for atleta in db if atleta['cpf'] == cpf]
    return db

# Endpoint para buscar todos os atletas com paginação
@app.get("/atletas/paginacao/", response_model=Page[AtletaResponse])
async def get_paginated_atletas(limit: int = 10, offset: int = 0):
    return paginate(db[offset: offset + limit])

# Endpoint para inserir um novo atleta
@app.post("/atletas/")
async def create_atleta(nome: str, cpf: str, centro_treinamento: str, categoria: str):
    try:
        # Simulação de inserção no banco de dados
        db.append({
            'nome': nome,
            'cpf': cpf,
            'centro_treinamento': centro_treinamento,
            'categoria': categoria
        })
        return {"message": "Atleta criado com sucesso"}
    except IntegrityError:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {cpf}")

# Exemplo de inicialização de dados
db = [
    {"nome": "Atleta1", "cpf": "11111111111", "centro_treinamento": "CT1", "categoria": "Categoria1"},
    {"nome": "Atleta2", "cpf": "22222222222", "centro_treinamento": "CT2", "categoria": "Categoria2"},
    {"nome": "Atleta3", "cpf": "33333333333", "centro_treinamento": "CT3", "categoria": "Categoria3"}
]

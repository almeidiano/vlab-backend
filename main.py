from fastapi import APIRouter, FastAPI
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from services.token import sign_jwt_token
from models.Item import Item
from utils.TipoCombustivel import PrecoCombustivel

app = FastAPI()

router = APIRouter(prefix="/api/v1")
security = HTTPBearer()

@router.get("/token")
async def login():
    return sign_jwt_token()

@router.post("/abastecimentos")
async def root(payload: Item):    
    combustivel = payload.tipo_combustivel.name
    
    # Regra de Negócio (Flag de Anomalia) checa se o preco_por_litro é +25% do preço original (enum PrecoCombustivel) 
    preco = payload.preco_por_litro
    
    if preco > (PrecoCombustivel[combustivel] * 1.25): 
        payload.improper_data = True
        
        return {"message": payload}
    else:
        return {"message": payload}

@router.get("/abastecimentos")
async def root(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    
    return {"message": "Conseguiu acessar.", "token": token}

@router.get("/motoristas/{cpf_motorista}/historico")
async def root(cpf_motorista: str, credentials: HTTPAuthorizationCredentials = Depends(security)):    
    return {"message": cpf_motorista}

app.include_router(router)
from utils.TipoCombustivel import TipoCombustivel
from pydantic import BaseModel, field_validator
from datetime import datetime
from validate_docbr import CPF

class Item(BaseModel):
    id_posto: int
    data_hora: datetime
    tipo_combustivel: TipoCombustivel
    preco_por_litro: float
    volume_abastecido: float
    cpf_motorista: str
    improper_data: bool = False

    @field_validator("cpf_motorista")
    def validate_cpf(cls, valor):
        cpf = CPF()
        if not cpf.validate(valor):
            raise ValueError("CPF inválido.")
        return valor
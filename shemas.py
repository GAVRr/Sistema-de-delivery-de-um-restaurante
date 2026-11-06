from pydantic import BaseModel
from typing import Optional, List



class UsuarioShema(BaseModel):
    nome : str
    email : str
    senha : str
    ativo : Optional[bool]
    admin : Optional[bool]

    class Config:
        from_atributes = True


class PedidoSchema(BaseModel):
    usuario: int

    class Config:
        from_atributes = True


class LoginSchema(BaseModel):
    email: str
    senha: str
    
    class Config:
        from_atributes = True

class ItempedidoSchema(BaseModel):
    quantidade : int
    sabor : str
    tamanho : str
    preco_unitario : float
    id_pedido : int

    class Config:
        from_atributes = True

class ResponsepedidoSchema(BaseModel):
    
    id :  int
    status : str
    preco : float
    

    class Config:
        from_atributes = True

    
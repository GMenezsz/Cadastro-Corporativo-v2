from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from hash import criar_hash, verificar_senha

from dados import inserir_usuario_corporativo, consultar_usuarios_corporativos, atualizar_usuario_corporativo, excluir_usuario_corporativo
from validacao_cadastros import validar_usuario, validar_senha

router = APIRouter()

class InserirUsuarioSchema(BaseModel):
    usuario: str
    senha: str

class ConsultarSchema(BaseModel):
    usuario: str

class AtualizarSchema(BaseModel):
    usuario_antigo: str
    senha_antiga: str
    novo_usuario: str
    nova_senha: str

class ExcluirSchema(BaseModel):
    usuario: str

@router.post("/cadastrar_usuario")
def cadastrar_usuario(dados: InserirUsuarioSchema):

    usuario_formatado = dados.usuario.strip().lower()

    if validar_usuario(usuario_formatado) is not True:
        raise HTTPException(status_code=400, detail="O usuário precisa ter no mínimo 6 caracteres.")

    if validar_senha(dados.senha) is not True:
        raise HTTPException(status_code=400, detail="A senha precisa conter no mínimo 6 caracteres.")

    senha_segura = criar_hash(dados.senha)

    inserir_usuario_corporativo(usuario_formatado, senha_segura)

    return {
        "mensagem": f"Usuário {usuario_formatado} criado com sucesso!"
    }

@router.post("/consultar_usuario")
def consulta_usuario(dados: ConsultarSchema):

    usuario_formatado = dados.usuario.strip().lower()

    if validar_usuario(usuario_formatado) is not True:
        raise HTTPException(status_code=400, detail="O usuário precisa ter no mínimo 6 caracteres.")

    resultado = consultar_usuarios_corporativos(usuario_formatado)

    if not resultado:
        raise HTTPException(status_code=400, detail="Usuário não encontrado.")
    
    return {
        "usuario": resultado
    }

@router.post("/atualizar_usuario")
def atualizar_usuario_senha(dados: AtualizarSchema):

    usuario_antigo_formatado = dados.usuario_antigo.strip().lower()
    usuario_formatado = dados.novo_usuario.strip().lower()

    if validar_usuario(usuario_antigo_formatado) is not True:
        raise HTTPException(status_code=400, detail="O usuário precisa ter no mínimo 6 caracteres.")

    if validar_senha(dados.senha_antiga) is not True:
                raise HTTPException(status_code=400, detail="A senha precisa conter no mínimo 6 caracteres.")
    
    if validar_usuario(usuario_formatado) is not True:
            raise HTTPException(status_code=400, detail="O usuário precisa ter no mínimo 6 caracteres.")

    if validar_senha(dados.nova_senha) is not True:
        raise HTTPException(status_code=400, detail="A senha precisa conter no mínimo 6 caracteres.")

    usuario_antigo = consultar_usuarios_corporativos(usuario_antigo_formatado)
    if not usuario_antigo:
        raise HTTPException(status_code=400, detail="Usuário não encontrado.")

    usuario_dados = usuario_antigo[0] 
    senha_salva = usuario_dados[2]

    if not verificar_senha(dados.senha_antiga, senha_salva):
        raise HTTPException(status_code=400, detail="Senha errada!")

    senha_segura = criar_hash(dados.nova_senha)

    atualizar_usuario_corporativo(usuario_antigo_formatado, usuario_formatado, senha_segura)

    return {
        "mensagem": "Usuário atualizado com sucesso!",
        "usuario": usuario_formatado
    }

@router.delete("/excluir_usuario")
def excluir_usuario(dados: ExcluirSchema):

    usuario_formatado = dados.usuario.strip().lower()

    if validar_usuario(usuario_formatado) is not True:
        raise HTTPException(status_code=400, detail="O usuário precisa ter no mínimo 6 caracteres.")

    usuario = consultar_usuarios_corporativos(usuario_formatado)

    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado.")

    excluir_usuario_corporativo(usuario_formatado)

    return {
        "mensagem": "Usuário deletado com sucesso!"
    }
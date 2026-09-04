from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from criptografia import criptografar, descriptografar

from dados import inserir_funcionarios, consultar_funcionarios, atualizar_funcionarios, excluir_funcionarios, consultar_funcionario_cpf
from validacao_cadastros import validar_cpf, validar_nome, validar_cargo, validar_data, validar_nacionalidade

router = APIRouter()

class FuncionarioSchema(BaseModel):
        nome_completo: str
        data_nascimento: str
        cpf: str
        nacionalidade: str
        cargo: str

class AtualizarSchema(BaseModel):
        cpf_antigo: str
        nome_novo: str
        data_nova: str
        cpf_novo: str
        nacionalidade_nova: str
        cargo_novo: str

class ConsultarSchema(BaseModel):
    cpf: str

class DeletarSchema(BaseModel):
    nome: str


@router.post("/cadastrar_funcionario")
def criar_funcionario(dados: FuncionarioSchema):

    nome_formatado = dados.nome_completo.strip().title()
    data_formatado = dados.data_nascimento.strip()

    cpf_formatado = dados.cpf.strip()

    nacionalidade_formatado = dados.nacionalidade.strip().title()
    cargo_formatado = dados.cargo.strip().title()

    if validar_nome(nome_formatado) is not True:
        raise HTTPException(status_code=400, detail="O nome precisa conter no mínimo 3 caracteres.")

    if validar_data(data_formatado) is not True:
        raise HTTPException(status_code=400, detail="Digite somente números na data de nascimento.")

    if validar_cpf(cpf_formatado) is not True:
        raise HTTPException(status_code=400, detail="Para CPF digite apenas números com caracteres igual a 11.")

    if validar_nacionalidade(nacionalidade_formatado) is not True:
        raise HTTPException(status_code=400, detail="Nacionalidade precisa ter no mínimo 3 caracteres.")

    if validar_cargo(cargo_formatado) is not True:
        raise HTTPException(status_code=400, detail="Cargo não pode ficar vazio.")

    cpf_seguro = criptografar(cpf_formatado)

    inserir_funcionarios(nome_formatado, data_formatado, cpf_seguro, nacionalidade_formatado, cargo_formatado)

    return {
        "mensagem": f"Colaborador {nome_formatado.split()[0]} cadastrado com sucesso!",
        "nome": nome_formatado,
        "cargo": cargo_formatado
    }

@router.put("/atualizar_funcionario")
def atualizar_dados_funcionario(dados: AtualizarSchema):

    cpf_digitado = dados.cpf_antigo.strip()

    nome_formatado = dados.nome_novo.strip().title()
    data_formatado = dados.data_nova.strip()

    cpf_formatado = dados.cpf_novo.strip()
    
    nacionalidade_formatado = dados.nacionalidade_nova.strip().title()
    cargo_formatado = dados.cargo_novo.strip().title()

    if validar_nome(nome_formatado) is not True:
            raise HTTPException(status_code=400, detail="O nome precisa conter no mínimo 3 caracteres.")
    
    if validar_data(data_formatado) is not True:
            raise HTTPException(status_code=400, detail="Digite somente números na data de nascimento.")
    
    if validar_cpf(cpf_formatado) is not True:
            raise HTTPException(status_code=400, detail="Para CPF digite apenas números com caracteres igual a 11.")
    
    if validar_nacionalidade(nacionalidade_formatado) is not True:
            raise HTTPException(status_code=400, detail="Nacionalidade precisa ter no mínimo 3 caracteres.")
    
    if validar_cargo(cargo_formatado) is not True:
            raise HTTPException(status_code=400, detail="Cargo não pode ficar vazio.")

    lista_cpfs = consultar_funcionarios()

    encontrou = False
    cpf_criptografado_alvo = None
    for cpf in lista_cpfs:
        cpf_criptografado = cpf[0]

        if descriptografar(cpf_criptografado) == cpf_digitado:
            encontrou = True
            cpf_criptografado_alvo = cpf_criptografado
            break

    if not encontrou:
        raise HTTPException(status_code=404, detail="Funcionário com o CPF antigo informado não foi encontrado.")
    
    cpf_seguro = criptografar(cpf_formatado)
    
    atualizar_funcionarios(nome_formatado, data_formatado, cpf_seguro, nacionalidade_formatado, cargo_formatado, cpf_criptografado_alvo)

    return {
        "mensagem": f"Colaborador {nome_formatado.split()[0]} atualizado com sucesso!",
        "nome": nome_formatado,
        "data": data_formatado,
        "cpf": cpf_formatado,
        "nacionalidade": nacionalidade_formatado,
        "cargo": cargo_formatado
    }

@router.post("/consultar_funcionario")
def consultar_dados_funcionario(dados: ConsultarSchema):


    cpf_digitado = dados.cpf.strip()

    if validar_cpf(cpf_digitado) is not True:
        raise HTTPException(status_code=400, detail="Para CPF digite apenas números com caracteres igual a 11.")

    lista_cpfs = consultar_funcionarios()
    
    encontrou = False
    cpf_criptografado_alvo = None
    for cpf in lista_cpfs:
        cpf_criptografado = cpf[0]
    
        if descriptografar(cpf_criptografado) == cpf_digitado:
            encontrou = True
            cpf_criptografado_alvo = cpf_criptografado
            break
    
    if not encontrou:
        raise HTTPException(status_code=404, detail="Funcionário com o CPF antigo informado não foi encontrado.")

    

    funcionarios = consultar_funcionario_cpf(cpf_digitado, cpf_criptografado_alvo)
    return {
        "funcionarios": funcionarios
    }

@router.delete("/deletar_funcionario")
def deletar_funcioanrio(dados: DeletarSchema):

    nome_formatado = dados.nome.strip().title()

    if validar_nome(nome_formatado) is not True:
        raise HTTPException(status_code=400, detail="O nome precisa conter no mínimo 3 caracteres.")

    excluir_funcionarios(nome_formatado)

    return {
        "mensagem": f"Funcionário {nome_formatado.split()[0]} excluído com sucesso!"
    }


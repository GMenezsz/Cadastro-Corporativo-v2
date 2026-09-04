def validar_cpf(cpf):

    cpf_formatado = cpf.replace(".", "").replace("-", "")

    if len(cpf_formatado) == 11 and cpf_formatado.isdigit():
        return True
    else:
        return False

def validar_nome(nome):
    if len(nome) >= 3:
        return True
    else:
        return False

def validar_data(data_nascimento):

    data_formatada = data_nascimento.replace("/", "")

    if len(data_formatada) == 8 and data_formatada.isdigit():
        return True
    else:
        return False

def validar_nacionalidade(nacionalidade):
    if len(nacionalidade) >= 3:
        return True
    else:
        return False

def validar_cargo(cargo):
    if not cargo:
        return False
    else:
        return True

def validar_usuario(usuario):
    if len(usuario) >= 6:
        return True
    else:
        return False

def validar_senha(senha):
    if len(senha) >= 6:
        return True
    else:
        return False
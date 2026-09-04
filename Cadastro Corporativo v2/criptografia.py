from cryptography.fernet import Fernet
import os

ARQUIVO_CHAVE = "chave.key"

# Se o arquivo da chave não existe, ele cria um novo automaticamente
if not os.path.exists(ARQUIVO_CHAVE):
    chave_gerada = Fernet.generate_key()
    with open(ARQUIVO_CHAVE, "wb") as arquivo:
        arquivo.write(chave_gerada)

# Lê a chave do arquivo para usar na API
with open(ARQUIVO_CHAVE, "rb") as arquivo:
    CHAVE = arquivo.read()

cifrador = Fernet(CHAVE)

def criptografar(cpf: str) -> str:
    return cifrador.encrypt(cpf.encode("utf-8")).decode("utf-8")

def descriptografar(cpf_cifrado: str) -> str:
    return cifrador.decrypt(cpf_cifrado.encode("utf-8")).decode("utf-8")
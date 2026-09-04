
# Nexus - Sistema de Gestão Corporativa e Autenticação

Sistema backend desenvolvido em **FastAPI** para gerenciamento de funcionários e controle de acesso corporativo, com foco em segurança de dados sensíveis (criptografia de CPFs e hashing seguro de senhas).

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI**: Framework web moderno e de alta performance para construção de APIs.
* **Uvicorn**: Servidor ASGI para execução da API.
* **SQLite3**: Banco de dados relacional leve e embutido.
* **Cryptographic (Fernet)**: Criptografia simétrica para proteção de dados sensíveis (CPF).
* **Bcrypt**: Hashing seguro e unidirecional para senhas corporativas.
* **Pydantic**: Validação de dados e tipagem em tempo de execução.

---

## 📁 Estrutura do Projeto

```text
bot/
│
├── main.py                    # Ponto de entrada da aplicação FastAPI
├── dados.py                   # Gerenciamento de conexões e tabelas SQLite
├── criptografia.py            # Funções de cifragem/decifragem (Fernet)
├── hash.py                    # Geração e verificação de hashes de senha (Bcrypt)
├── validacao_cadastros.py     # Regras de validação (CPF, nome, datas, etc.)
│
├── routers/                   # Endpoints da API divididos por domínio
│   ├── cadastro_funcionario.py# Rotas CRUD de funcionários
│   └── login_corporativo.py   # Rotas de cadastro, consulta e atualização de usuários
│
├── corporativo.db             # Banco de dados SQLite (gerado automaticamente)
└── chave.key                  # Chave de criptografia Fernet (gerada automaticamente)
```

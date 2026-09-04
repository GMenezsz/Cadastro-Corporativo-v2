from fastapi import FastAPI
from dados import criar_banco
from routers import login_corporativo, cadastro_funcionario

app = FastAPI(title="Nexus - Cadastro de Funcionários")

criar_banco()

app.include_router(login_corporativo.router)
app.include_router(cadastro_funcionario.router)
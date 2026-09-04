import sqlite3

funcionarios = """
    CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    nacionalidade TEXT NOT NULL,
    cargo TEXT NOT NULL
    )"""

login_corporativo = """
    CREATE TABLE IF NOT EXISTS login_corporativo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
    )"""

def criar_banco():
    conn = sqlite3.connect("corporativo.db")
    cursor = conn.cursor()
    cursor.execute(login_corporativo)
    cursor.execute(funcionarios)
    conn.commit()
    conn.close()

# --------------------------------------------
# -------------- FUNCIONARIOS ----------------
# --------------------------------------------

def inserir_funcionarios(nome_completo, data_nascimento, cpf, nacionalidade, cargo):
    conn = sqlite3.connect("corporativo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO funcionarios (nome_completo, data_nascimento, cpf, nacionalidade, cargo) VALUES (?, ?, ?, ?, ?)",
                (nome_completo, data_nascimento, cpf, nacionalidade, cargo))
    conn.commit()
    conn.close()

def consultar_funcionarios():
    conn = sqlite3.connect("corporativo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT cpf FROM funcionarios")
    funcionarios = cursor.fetchall()
    conn.close()
    return funcionarios

def consultar_funcionario_cpf(cpf_digitado, cpf_cifrado):
    conn = sqlite3.connect("corporativo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionarios WHERE cpf = ?", (cpf_cifrado,))
    funcionarios = cursor.fetchall()
    conn.close()
    return funcionarios

def atualizar_funcionarios(nome_completo, data_nascimento, cpf_novo, nacionalidade, cargo, cpf_cifrado_antigo):
    conn = sqlite3.connect("corporativo.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE funcionarios 
        SET nome_completo = ?, data_nascimento = ?, cpf = ?, nacionalidade = ?, cargo = ? 
        WHERE cpf = ?
        """, 
        (nome_completo, data_nascimento, cpf_novo, nacionalidade, cargo, cpf_cifrado_antigo)
    )
    conn.commit()
    conn.close()

def excluir_funcionarios(nome_completo):
    conn = sqlite3.connect("corporativo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM funcionarios WHERE nome_completo = ?", (nome_completo,))
    conn.commit()
    conn.close()

# --------------------------------------------
# -------------- CORPORATIVO -----------------
# --------------------------------------------

def inserir_usuario_corporativo(usuario, senha):
    conn = sqlite3.connect("corporativo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO login_corporativo (usuario, senha) VALUES (?, ?)",
                (usuario, senha))
    conn.commit()
    conn.close()

def consultar_usuarios_corporativos(usuario):
    conn = sqlite3.connect("corporativo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login_corporativo WHERE usuario = ?", (usuario,))
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def atualizar_usuario_corporativo(usuario_antigo, novo_usuario, nova_senha):
    conn = sqlite3.connect("corporativo.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE login_corporativo SET usuario = ?, senha = ? WHERE usuario = ?", (novo_usuario, nova_senha, usuario_antigo,))
    conn.commit()
    conn.close()

def excluir_usuario_corporativo(usuario):
    conn = sqlite3.connect("corporativo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM login_corporativo WHERE usuario = ?", (usuario,))
    conn.commit()
    conn.close()
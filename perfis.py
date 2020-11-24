def encriptar(password):
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()

def tem_password(dicionario, id, password):
    return id in dicionario and get_password(dicionario, id) == encriptar(password)

def adiciona_utilizador(perfis, id, nome, password):
	assert id not in perfis, f"Erro: utilizador {id} já existe!"
	ficha = {}
	ficha['nome'] = nome
	ficha['password'] = encriptar(password)
	perfis[id] = ficha	

def get_nome(perfis, id):
    return perfis[id]['nome']

def get_password(perfis, id):
    return perfis[id]['password']

def criar_utilizador(id, nome, password):
    perfis = ler_perfis()
    adiciona_utilizador(perfis, id, nome, password)
    escrever_perfis(perfis)

def autenticacao():
    """Faz o procedimento de autenticação"""
    pass

def ler_perfis():
    pass

def escrever_perfis(perfis):
    pass

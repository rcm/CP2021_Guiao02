def encriptar(password):
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()

def tem_password(dicionario, id, password):
    """
    """
    return id in dicionario and get_password(dicionario, id) == encriptar(password)

def adiciona_utilizador(perfis, id, nome, password):
    """
    Adiciona um utilizador ao dicionário dos perfis

    Parameters
    ----------
    perfis: dict[str, dict[str, str]]
        Dicionário em que a chave é o identificador e o valor é um dicionário com os campos nome e password
    id: str
        Identificador do utilizador
    nome: str
        Nome do utilizador
    password: str
        Password do utilizador
    Returns
    -------
    dict[str, dict[str, str]]
        Dicionário com mais um registo correspondendo ao utilizador que foi adicionado
    """
    assert id not in perfis, f"Erro: utilizador {id} já existe!"
    ficha = {}
    ficha['nome'] = nome
    ficha['password'] = encriptar(password)
    perfis[id] = ficha
    return perfis

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
    perfis = {}
    with open('PERFIS') as F:
        for linha in F:
            linha = linha.strip()
            id, nome, pwd = linha.split(':')
            perfis[id] = {'nome' : nome, 'password' : pwd}
    return perfis
        

def escrever_perfis(perfis):
    with open('PERFIS', 'w') as F:
        for id in perfis:
            print(id, get_nome(perfis, id), get_password(perfis, id), sep = ':', file = F)

# Caso corra este módulo diretamente, isto é executado
if __name__ == '__main__':
    autenticacao()

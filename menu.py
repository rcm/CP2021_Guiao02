def escolher_opcao(num_opcoes):
    while True:
        n = input('Introduza a sua opção: ')
        if n.isnumeric():
            n = int(n) - 1
            if n >= 0 and n < num_opcoes:
                return n

def menu(opcoes):
    """
    Mostra o menu e permite escolher uma opção

    Parameters
    ----------
    opcoes: list[(str, fun)]
        Lista de tuplos com a mensagem a ser mostrada e a função a ser invocada
    Returns
    -------
    var
        O valor que for devolvido pela função
    """
    for n, opcao in enumerate(opcoes):
        texto, funcao = opcao
        print(n + 1, texto)
    escolha = escolher_opcao(len(opcoes))
    texto, funcao = opcoes[escolha]
    return funcao()

if __name__ == '__main__':
    def administrador():
        return menu([])
    def jogador():
        return menu([])

    print(menu([
        ('Administrador', administrador),
        ('Jogador', jogador),
        ('Sair', exit)]))

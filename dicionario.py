def ler_dicionario():
    palavras = []
    with open('DICIONARIO') as F:
        for linha in F:
            palavras.append(linha.strip())
        return palavras

def tem_palavra(palavra):
    return palavra in ler_dicionario()

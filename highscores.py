def ler_highscores():
    scores = []
    with open('HIGHSCORES') as F:
        for linha in F:
            id, score = linha.split()
            score = int(score)
            scores.append((score, id))
    return scores

def escrever_highscores(scores):
    with open('HIGHSCORES', 'w') as F:
        for score, id in scores:
            print(id, score, file = F)
            
def adiciona_score(id, score):
    scores = ler_highscores()
    scores.append((score, id))
    scores = sorted(scores, reverse = True)
    escrever_highscores(scores)

def imprimir_highscores():
    for score, id in ler_highscores():
        print(id, score)

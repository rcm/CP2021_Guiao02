def ler_highscores():
    pass

def escrever_highscores():
    pass

def adiciona_score(id, score):
    scores = ler_highscores()
    scores.append((score, id))
    scores = sorted(scores, reverse = True)
    escrever_highscores(scores)

import unittest

from perfis import *
from dicionario import *
from highscores import *

def guardar(ficheiro):
    with open(ficheiro) as F:
        return F.read()
def restaurar(ficheiro, conteudo):
    with open(ficheiro, 'w') as F:
        F.write(conteudo)

class Test(unittest.TestCase):
    def setUp(self):
        """ guardar o estado dos 3 ficheiros"""
        self.dicionario = guardar('DICIONARIO')
        self.perfis = guardar('PERFIS')
        self.highscores = guardar('HIGHSCORES')

        """Criar os 3 ficheiros com valores por omissão"""
        restaurar('PERFIS', """admin:Administrador:dc24df8119fadb637178d5e959887ce3
""")
        restaurar('DICIONARIO', """abomasnow
abra
absol
accelgor
aegislash
aerodactyl
""")
        restaurar('HIGHSCORES', "")
    def tearDown(self):
        restaurar('DICIONARIO', self.dicionario)
        restaurar('PERFIS', self.perfis)
        restaurar('HIGHSCORES', self.highscores)
        
    def test_adiciona_utilizador(self):
        perfis = {}
        adiciona_utilizador(perfis, 'rcm', 'Rui Mendes', 'tubarao epiletico')
        self.assertEqual(len(perfis), 1)
        self.assertTrue('rcm' in perfis)
        self.assertEqual(get_nome(perfis, 'rcm'), 'Rui Mendes')
        self.assertTrue(tem_password(perfis, 'rcm','tubarao epiletico'))        
    def test_criar_utilizador(self):
        criar_utilizador('rcm', 'Rui Mendes', 'tubarao epiletico')
        with open('PERFIS') as F:
            linhas = F.readlines()

        print(linhas)
        ult_linha = linhas[-1]
        self.assertEqual(ult_linha, f"rcm:Rui Mendes:{encriptar('tubarao epiletico')}\n")


    def test_ler_dicionario(self):
        obtained = ler_dicionario()
        expected = "abomasnow abra absol accelgor aegislash aerodactyl".split()
        self.assertEqual(expected, obtained)
    def test_tem_palavra(self):
        palavras = "abomasnow abra absol accelgor aegislash aerodactyl".split()
        outras = "batatas cebolas repolhos".split()
        for palavra in palavras:
            self.assertTrue(tem_palavra(palavra))
        for palavra in outras:
            self.assertFalse(tem_palavra(palavra))

    def test_highscore(self):
        adiciona_score('rcm', 40)
        adiciona_score('rcm', 50)
        adiciona_score('rcm', 20)
        self.assertEqual(ler_highscores(), [(50, 'rcm'),(40, 'rcm'),(20, 'rcm')])
        
if __name__ == '__main__':
    unittest.main()

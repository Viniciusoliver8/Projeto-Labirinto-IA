from mazelib import Maze
from mazelib.generate.BacktrackingGenerator import BacktrackingGenerator

def gerar_labirinto(linhas: int, colunas: int):
    """
    Gera um labirinto usando a biblioteca mazelib com o algoritmo Recursive Backtracker.
    
    linhas: Número de linhas do labirinto.
    colunas: Número de colunas do labirinto.
    
    Retorna:
        grid: Labirinto gerado, onde 0 é caminho livre e 1 é obstáculo.
    """
    m = Maze()
    m.generator =  BacktrackingGenerator(linhas, colunas)
    m.generate()
    
    return m.grid
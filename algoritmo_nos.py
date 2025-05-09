from math import sqrt
from typing import Tuple, Dict

def criar_no(posicao: Tuple[int, int], g: float = float('inf'), 
             h: float = 0.0, pai: Dict = None) -> Dict:
    """
    Cria um nó para o algoritmo A*.
    
    posicao: (x, y) coordenadas do nó.
    g: Custo do caminho do início até esse nó (padrão: infinito).
    h: Custo estimado do nó até o objetivo (padrão: 0).
    pai: Nó pai (padrão: None).
    
    Retorna:
        Dicionário com as informações do nó.
    """
    return {
        'posicao': posicao,
        'g': g,
        'h': h,
        'f': g + h,
        'pai': pai
    }

def calcular_heuristica(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
    """
    Calcula a distância estimada entre dois pontos usando a distância Euclidiana.
    """
    x1, y1 = pos1
    x2, y2 = pos2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

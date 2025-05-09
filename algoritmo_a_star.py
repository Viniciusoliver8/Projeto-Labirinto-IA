import heapq
from typing import List, Tuple, Dict
from algoritmo_nos import criar_no, calcular_heuristica

def obter_vizinhos_validos(grid: List[List[int]], posicao: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Obtém todos os vizinhos válidos (sem obstáculos) de uma posição.
    
    grid: Grade do labirinto (0 = caminho livre, 1 = obstáculo).
    posicao: Posição atual (x, y).
    
    Retorna:
        Lista de posições válidas para os vizinhos.
    """
    x, y = posicao
    linhas, colunas = len(grid), len(grid[0])
    
    movimentos_possiveis = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    
    return [
        (nx, ny) for nx, ny in movimentos_possiveis
        if 0 <= nx < linhas and 0 <= ny < colunas and grid[nx][ny] == 0
    ]

def reconstruir_caminho(no_objetivo: Dict) -> List[Tuple[int, int]]:
    """
    Reconstrói o caminho a partir do nó objetivo, seguindo os nós pais.
    """
    caminho = []
    atual = no_objetivo
    
    while atual is not None:
        caminho.append(atual['posicao'])
        atual = atual['pai']
        
    return caminho[::-1]  

def buscar_caminho(grid: List[List[int]], inicio: Tuple[int, int], objetivo: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Encontra o caminho ótimo usando o algoritmo A*.
    
    grid: Grade do labirinto (0 = caminho livre, 1 = obstáculo).
    inicio: Posição de início (x, y).
    objetivo: Posição objetivo (x, y).
    
    Retorna:
        Lista de posições representando o caminho ótimo.
    """
    # Inicializa o nó de início
    no_inicio = criar_no(inicio, g=0, h=calcular_heuristica(inicio, objetivo))
    
    # Listas abertas e fechadas
    lista_aberta = [(no_inicio['f'], inicio)]  # Fila de prioridade
    dicionario_aberto = {inicio: no_inicio}  # Para consulta rápida
    conjunto_fechado = set()  # Conjunto de nós explorados
    
    while lista_aberta:
        # Pega o nó com o menor valor f
        _, posicao_atual = heapq.heappop(lista_aberta)
        no_atual = dicionario_aberto[posicao_atual]
        
        # Verifica se chegou ao objetivo
        if posicao_atual == objetivo:
            return reconstruir_caminho(no_atual)
        
        conjunto_fechado.add(posicao_atual)
        
        # Explora os vizinhos
        for vizinho_pos in obter_vizinhos_validos(grid, posicao_atual):
            if vizinho_pos in conjunto_fechado:
                continue
            
            g_tentativo = no_atual['g'] + calcular_heuristica(posicao_atual, vizinho_pos)
            
            if vizinho_pos not in dicionario_aberto:
                vizinho = criar_no(vizinho_pos, g=g_tentativo, h=calcular_heuristica(vizinho_pos, objetivo), pai=no_atual)
                heapq.heappush(lista_aberta, (vizinho['f'], vizinho_pos))
                dicionario_aberto[vizinho_pos] = vizinho
            elif g_tentativo < dicionario_aberto[vizinho_pos]['g']:
                vizinho = dicionario_aberto[vizinho_pos]
                vizinho['g'] = g_tentativo
                vizinho['f'] = g_tentativo + vizinho['h']
                vizinho['pai'] = no_atual
    
    return []  # Nenhum caminho encontrado

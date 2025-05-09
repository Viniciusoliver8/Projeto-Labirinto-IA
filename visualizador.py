import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple

def visualizar_labirinto(grid: List[List[int]], caminho: List[Tuple[int, int]] = []):
    """
    Visualiza o labirinto e o caminho encontrado.
    grid: A grade do labirinto.
    caminho: Lista de posições representando o caminho
    """
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap='binary')
    
    if caminho:
        caminho = np.array(caminho)
        plt.plot(caminho[:, 1], caminho[:, 0], 'b-', linewidth=3, label='Caminho')
        plt.plot(caminho[0, 1], caminho[0, 0], 'go', markersize=15, label='Início')
        plt.plot(caminho[-1, 1], caminho[-1, 0], 'ro', markersize=15, label='Objetivo')
    
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.title("Resultado da Busca A* no Labirinto")
    plt.show()

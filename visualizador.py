import matplotlib.pyplot as plt
import numpy as np
import os
from typing import List, Tuple

def visualizar_labirinto(grid: List[List[int]], caminho: List[Tuple[int, int]] = []):
    """
    Visualiza o labirinto e o caminho encontrado.
    grid: A grade do labirinto.
    caminho: Lista de posições representando o caminho
    """
    # Verifica se existe o diretorio.
    if not os.path.exists('resultados_img'):
        os.makedirs('resultados_img')  # Mesma coisa que "mkdir resultados_img"

    count = len([f for f in os.listdir('resultados_img') if f.endswith('.png')]) # faz a contagem de quantos arquivos com final .png existe para implementar na proxima contagem

    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap='binary')

    if caminho:
        caminho = np.array(caminho)

        plt.plot(caminho[:, 1], caminho[:, 0], 'b-', linewidth=3, label='Caminho')
        plt.scatter(caminho[:, 1], caminho[:, 0], color='gray', s=50, zorder=5, label='Passos')
        plt.plot(caminho[0, 1], caminho[0, 0], 'go', markersize=15, label='Início')
        plt.plot(caminho[-1, 1], caminho[-1, 0], 'ro', markersize=15, label='Objetivo')

    #texto bottom
    total_passos = len(caminho)
    plt.subplots_adjust(bottom=0.15)
    plt.figtext(0.5, 0.05, f"Total de passos realizados até chegar ao objetivo: {total_passos}",
                horizontalalignment='center', verticalalignment='center', fontsize=14)

    plt.grid(True)
    plt.legend(fontsize=12)
    plt.title("Resultado da Busca A* no Labirinto")

    plt.savefig(f"resultados_img/labirinto_{count + 1}_image.png")
    plt.close()

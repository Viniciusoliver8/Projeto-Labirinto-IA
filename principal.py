from gerador_labirinto import gerar_labirinto
from algoritmo_a_star import buscar_caminho
from visualizador import visualizar_labirinto
import random

# Gera o labirinto
linhas = 20
colunas = 20
labirinto = gerar_labirinto(linhas, colunas)

# Garante que o início e o objetivo não são obstáculos
inicio = (1, 1)
objetivo = (linhas - 2, colunas - 2)

while labirinto[inicio[0]][inicio[1]] == 1 or labirinto[objetivo[0]][objetivo[1]] == 1:
    inicio = (random.randint(0, linhas-1), random.randint(0, colunas-1))
    objetivo = (random.randint(0, linhas-1), random.randint(0, colunas-1))

# Encontra o caminho usando A*
caminho = buscar_caminho(labirinto, inicio, objetivo)

# Exibe o resultado
if caminho:
    print(f"Caminho encontrado com {len(caminho)} passos!")
    visualizar_labirinto(labirinto, caminho)
else:
    print("Nenhum caminho encontrado!")

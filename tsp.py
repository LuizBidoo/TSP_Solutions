import sys
import time
from itertools import permutations, pairwise


def peso_do_caminho(caminho, matrix):
    peso = 0
    duplas = pairwise(caminho)
    for dupla in duplas:
        aresta = matrix[dupla[0]][dupla[1]]
        if aresta == 0: return 0
        peso += aresta
    arestaInicio = matrix[caminho[len(caminho)-1]][caminho[0]]
    if arestaInicio == 0 : return 0
    peso += arestaInicio
    return peso

def peso_do_caminho(caminho, matrix):
    peso = 0
    for i in range(len(caminho)-1):
        peso += matrix[caminho[i]][caminho[i+1]]
    peso += matrix[caminho[-1]][caminho[0]]
    return peso                        
def tsp_complete(matrix):
    best_line = None
    lowest_sum = sys.maxsize
    size_matrix = len(matrix)
    numeros = list(range(size_matrix))
    for combinacao in permutations(range(size_matrix)):
        peso = peso_do_caminho(combinacao, matrix)
        if peso < lowest_sum and peso != 0:
            lowest_sum = peso
            best_line = combinacao
    return lowest_sum, best_line

def ler_matriz_adjacencia(caminho_do_arquivo):
    matriz_adjacencia = []
    with open(caminho_do_arquivo, "r") as file:
        for linha in file:
            linha_convertida = list(map(int, linha.strip().split()))
            matriz_adjacencia.append(linha_convertida)
    return matriz_adjacencia

def main():
    if len(sys.argv) != 2:
        print("Número de argumentos incorreto. Utilize:")
        print("python tsp.py <caminho_do_arquivo>")
        exit(1)

    caminho_do_arquivo = sys.argv[1]
    print(f"Lendo arquivo: {caminho_do_arquivo}")
    matriz_adjacencia = ler_matriz_adjacencia(caminho_do_arquivo)
    #print("Matriz de Adjacência:")
    #
    #for linha in matriz_adjacencia:
    #    print(linha)
    inicio = time.time()
    peso, caminho = tsp_complete(matriz_adjacencia)
    fim = time.time()
    print(f"Tempo do algoritmo completo para {caminho_do_arquivo} = {fim - inicio}")
    print(f'{peso}, {caminho}')

main()

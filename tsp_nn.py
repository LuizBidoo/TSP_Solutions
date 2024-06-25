import sys
from math import inf
import time

def ler_matriz_adjacencia(caminho_do_arquivo):
    matriz_adjacencia = []  # inicia matriz vazia
    with open(caminho_do_arquivo, "r") as file:  # abre arquivo para a leitura
        for linha in file:
            linha_convertida = list(map(int, linha.strip().split()))  # transforma cada linha em uma matriz de inteiros
            matriz_adjacencia.append(linha_convertida)
    return matriz_adjacencia

def nearest_neighboor(matriz_adjacencia, inicio):
    custo = 0  # custo inicial
    visitados = []  # lista de visitados
    vertice_atual = inicio  # vertice atual
    custo_parcial = 0  # custo parcial

    # primeira viagem
    vertice_atual, custo_parcial = calcular_distancia(matriz_adjacencia, visitados, vertice_atual)
    custo += custo_parcial
    visitados.append(vertice_atual)

    # resto das viagens de ida
    while len(visitados) != len(matriz_adjacencia):
        vertice_atual, custo_parcial = calcular_distancia(matriz_adjacencia, visitados, vertice_atual)
        custo += custo_parcial
        visitados.append(vertice_atual)

    custo_parcial = matriz_adjacencia[vertice_atual][inicio]
    custo += custo_parcial
    visitados.append(inicio)
    
    return custo, visitados


def calcular_distancia(matriz_adjacencia, visitados, vertice_atual):
    custo_minimo = inf
    menor_vertice = -1
    for vertice, custo in enumerate(matriz_adjacencia[vertice_atual]):
        if vertice not in visitados and custo < custo_minimo:
            custo_minimo = custo
            menor_vertice = vertice

    return menor_vertice, custo_minimo


def main():
    if len(sys.argv) != 2:
        print("Número de argumentos incorreto. Utilize:")
        print("python tsp_nn.py <caminho_do_arquivo>")
        exit(1)

    caminho_do_arquivo = sys.argv[1]
    print(f"Lendo arquivo: {caminho_do_arquivo}")
    matriz_adjacencia = ler_matriz_adjacencia(caminho_do_arquivo)
    print("Matriz de Adjacência:")
    for linha in matriz_adjacencia:
        print(linha)

    # solicitando entradas do usuário até que uma resposta válida seja passada
    while True:
        try:
            inicio = int(input("Escolha o vértice inicial para a aplicação do algoritmo Nearest Neighbor: "))
            if inicio < 0 or inicio >= len(matriz_adjacencia):
                raise ValueError("Vértice arbitário inexistente")
            break  
        except ValueError:
            print("Entrada inválida. Por favor, forneça um número inteiro válido.")
    tempo_inicial = time.time()
    custo, caminho = nearest_neighboor(matriz_adjacencia, inicio)
    tempo_final = time.time()
    print(f"Custo mínimo sub-óptimo = {custo}\n")
    print("Caminho percorrido:", end=" ")
    for vertice in caminho:
        print(vertice, end=" ")
    print(f"\nTempo de execução em segundos = {tempo_final - tempo_inicial}")

if __name__ == "__main__":
    main()


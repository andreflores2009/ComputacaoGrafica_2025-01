# -*- coding: utf-8 -*-
"""Exemplo02_matriz_Diagonal.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13lz5NLi_zuZappKmvKyYMIIKL7PqUCKF
"""

# Importa a biblioteca NumPy para facilitar a manipulação de matrizes
import numpy as np

# Define a matriz A
A = np.array([[2, 0, 0],
              [0, 1, 0],
              [0, 0, 7]])

# Exibe a matriz inicial
print("Matriz A:")
print(A)

# Obtém as dimensões da matriz
linhas, colunas = A.shape

# Verifica se a matriz é quadrada (condição necessária para ser diagonal)
if linhas != colunas:
    print("\nA matriz não é quadrada, portanto, não pode ser diagonal.")
else:
    # Variável para indicar se é diagonal
    eh_diagonal = True

    # Percorre a matriz verificando se os elementos fora da diagonal são zero
    for i in range(linhas):
        for j in range(colunas):
            if i != j and A[i][j] != 0:  # Se houver elemento não-diagonal diferente de zero
                eh_diagonal = False
                break

    # Exibe o resultado
    if eh_diagonal:
        print("\nA matriz é diagonal.")
    else:
        print("\nA matriz não é diagonal.")
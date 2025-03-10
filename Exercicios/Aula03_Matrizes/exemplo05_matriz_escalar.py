# -*- coding: utf-8 -*-
"""Exemplo05_matriz_escalar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14Ume_I0MZv0LwjJ6d1GUjRzWiSGbI9sa

Exercício 05 - Matriz por um múltiplo escalar x=3
"""

# Importa a biblioteca NumPy para facilitar a manipulação de matrizes
import numpy as np

# Define a matriz A
A = np.array([[2, 3, 8],
              [6, 0, 4],
              [1, 5, 7]])

# Define o escalar x
x = 3

# Exibe a matriz original
print("Matriz A:")
print(A)

# Obtém as dimensões da matriz
linhas, colunas = A.shape

# Inicializa a matriz resultado com as mesmas dimensões de A
resultado = np.zeros((linhas, colunas), dtype=int)

# Multiplica a matriz A pelo escalar x manualmente
for i in range(linhas):  # Percorre as linhas da matriz
    for j in range(colunas):  # Percorre as colunas da matriz
        resultado[i][j] = A[i][j] * x  # Multiplica cada elemento pelo escalar

# Exibe o resultado da multiplicação
print("\nResultado da multiplicação de A por", x, ":")
print(resultado)
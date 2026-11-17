print("Algoritmo para calcular o determinante de uma matriz 2x2")
print()
matriz = [
    [int(input("Informe o valor de A: ")), int(input("Informe o valor de B: "))],
    [int(input("Informe o valor de C: ")), int(input("Informe o valor de D: "))]
]
det = (matriz[0][0]*matriz[1][1]) - (matriz[0][1]*matriz[1][0])
print("Matriz informada: ")
for i in matriz:
    print(i)
print(f"O determinante da matriz é {det}")
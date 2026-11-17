print("Algoritmo para somar duas matrizes 4X3")
print()
matriz_1 = [
    [int(input("Informe o valor da posição 1,1: ")), int(input("Informe o valor da posição 1,2: ")), int(input("Informe o valor da posição 1,3: "))],
    [int(input("Informe o valor da posição 2,1: ")), int(input("Informe o valor da posição 2,2: ")), int(input("Informe o valor da posição 2,3: "))],
    [int(input("Informe o valor da posição 3,1: ")), int(input("Informe o valor da posição 3,2: ")), int(input("Informe o valor da posição 3,3: "))],
    [int(input("Informe o valor da posição 4,1: ")), int(input("Informe o valor da posição 4,2: ")), int(input("Informe o valor da posição 4,3: "))]
]
matriz_2 = [
    [int(input("Informe o valor da posição 1,1: ")), int(input("Informe o valor da posição 1,2: ")), int(input("Informe o valor da posição 1,3: "))],
    [int(input("Informe o valor da posição 2,1: ")), int(input("Informe o valor da posição 2,2: ")), int(input("Informe o valor da posição 2,3: "))],
    [int(input("Informe o valor da posição 3,1: ")), int(input("Informe o valor da posição 3,2: ")), int(input("Informe o valor da posição 3,3: "))],
    [int(input("Informe o valor da posição 4,1: ")), int(input("Informe o valor da posição 4,2: ")), int(input("Informe o valor da posição 4,3: "))]
]
matriz_soma = [
    [(matriz_1[0][0]+matriz_2[0][0]), (matriz_1[0][1]+matriz_2[0][1]), (matriz_1[0][2]+matriz_2[0][2])],
    [(matriz_1[1][0]+matriz_2[1][0]), (matriz_1[1][1]+matriz_2[1][1]), (matriz_1[1][2]+matriz_2[1][2])],
    [(matriz_1[2][0]+matriz_2[2][0]), (matriz_1[2][1]+matriz_2[2][1]), (matriz_1[2][2]+matriz_2[2][2])],
    [(matriz_1[3][0]+matriz_2[3][0]), (matriz_1[3][1]+matriz_2[3][1]), (matriz_1[3][2]+matriz_2[3][2])]
]
print("A soma das matrizes é: ")
for i in matriz_soma:
    print(i)
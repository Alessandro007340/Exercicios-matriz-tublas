print("Algoritmo para calcular determinante de matriz 3x3")
print()
matriz = []
for i in range(3):
    linha = []
    for j in range(3): 
        valor = int(input(f"Informe o valor da posição {i+1}, {j+1}: "))
        linha.append(valor)
    matriz.append(linha)
det = (matriz[0][0]*matriz[1][1]*matriz[2][2]+matriz[0][1]*matriz[1][2]*matriz[2][0]+matriz[0][2]*matriz[1][0]*matriz[2][1]-
       matriz[0][2]*matriz[1][1]*matriz[2][0]-matriz[0][1]*matriz[1][0]*matriz[2][2]-matriz[0][0]*matriz[1][2]*matriz[2][1]
       )
print(f"O determinante da matriz informada é {det}")
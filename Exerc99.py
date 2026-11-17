print("Algoritmo para verificar pessoas com 18 anos ou mais")
print()
pessoas = []
for i in range(10):
    nome = str(input(f"Informe o nome da {i+1}° pessoa: "))
    idade = int(input(f"Informe a idade de {nome}: "))
    pessoas.append((nome, idade))
print("Pessoas com menos de 18 anos: ")
for i in pessoas:
    if i[1] < 18:
        print(f"Nome - {i[0]}, idade - {i[1]}")
print("Pessoas com mais de 18 anos: ")
for i in pessoas:
    if i[1] >= 18:
        print(f"nome - {i[0]}, idade - {i[1]}")
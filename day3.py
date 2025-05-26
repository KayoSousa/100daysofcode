## day3 - Input and Output

nome = input("Por favor, insira o seu nome: ")
print("Olá, ", nome)

idade = int(input("Qual a sua idade? "))
altura = float(input("Informe a sua altura, por favor: "))

print("\nSeus dados, são:")
print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)

print("\nTipos de Dados:")
print("Nome: ", type(nome))
print("Idade: ", type(idade))
print("Altura: ", type(altura))
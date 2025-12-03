import random

print("----sistema senha aleatorias------")

letrasMaiusculas = "ABCDEFGHIJKMNOPQRSTUVWXYZ"
letrasMinusculas = "abcdefghijkmnopqrstuvwxyz"
simbolos = "@!#&$*()+="

while True:
    tamanho_senha = int(input("Digite o tamanho da senha que deseja:"))
    todosCaracters = letrasMaiusculas+letrasMinusculas+simbolos
    senhaAleatoria = ""

    for i in range(tamanho_senha):
      senhaAleatoria += random.choice(todosCaracters)
    break

print("Senha aleatoria:" , senhaAleatoria)






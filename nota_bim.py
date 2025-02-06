soma = 0.0
i = 0
print ("Digite as quatro notas bimestrais e saiba a média do aluno: ")
while i < 4:
    nota = input(f"Digite a nota do {i+1}º bimestre: ")
    try:
        numero = float(nota)
    except ValueError:
        print("Erro: o valor digitado não é um número!")
        break
    if numero > 10.0 or numero < 0.0:
        print("A nota não pode ser maior do que 10 ou menor do que 0!")
    else:
        soma = soma + numero
        i = i + 1
print(f"A média arredondada é {round(soma/4):.2f}")
print("Tendo a altura de uma pessoa, veja seu peso ideal!")
altura_pessoa = float(input("Insira a altura em metros: "))
print(f"O peso ideal para a altura de {altura_pessoa:.2f} m em um homem é de: {round((72.7*altura_pessoa)-58)}kg")
print(f"O peso ideal para a altura de {altura_pessoa:.2f} m em uma mulher é de: {round((62.1*altura_pessoa)-44.7)}kg")
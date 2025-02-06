print("Tendo a altura de uma pessoa, veja seu peso ideal!")
altura_pessoa = float(input("Insira a altura em metros: "))
print(f"O peso ideal para a altura de {altura_pessoa:.2f} m é de: {round((72.7*altura_pessoa)-58)}kg")
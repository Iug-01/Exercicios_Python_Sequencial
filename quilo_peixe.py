peso = 0.0
peso = float(input("Insira o peso total dos peixes: "))
if peso > 50: 
    peso = peso - 50
    print(f"A multa a ser paga é de R$ {peso * 4:.2f}")
else:
    print("Não há multa a ser paga!")
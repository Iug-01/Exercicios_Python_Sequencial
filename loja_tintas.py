area_pintada = float(input("Insira a área a ser pintada em m²: "))
numero_galoes = area_pintada/54
valor_gasto = numero_galoes * 80
if numero_galoes//1 != numero_galoes:
    numero_galoes = (numero_galoes//1) + 1
    valor_gasto = numero_galoes * 80
    print(f"A quantidade de galões necessários é {numero_galoes:,.0f} e o custo total é de R$ {valor_gasto:,.0f}".replace(",","-").replace(".",",").replace("-","."))

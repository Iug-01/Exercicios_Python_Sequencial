area_pintada = float(input("Insira a área a ser pintada em m²: "))
litros_tinta = area_pintada/6
numero_galoes18 = litros_tinta/18
numero_galoes36 = litros_tinta/3.6
resto18 = numero_galoes18 - numero_galoes18//1
resto36 = numero_galoes36 - numero_galoes36//1
if numero_galoes18//1 != numero_galoes18:
    numero_galoes18 = numero_galoes18//1 + 1
    numero_galoes36 = numero_galoes36//1 + 1
valor_gasto18 = numero_galoes18 * 80
valor_gasto36 = numero_galoes36 * 25
print(f"A quantidade necessária de galões de 18 litros é {numero_galoes18:,.2f} e o custo total é de R$ {valor_gasto18:,.2f}".replace(",","-").replace(".",",").replace("-","."))
print(f"A quantidade necessária de galões de 3,6 litros é {numero_galoes36:,.2f} e o custo total é de R$ {valor_gasto36:,.2f}".replace(",","-").replace(".",",").replace("-","."))
print(f"A quantidade necessária de galões de 18 e 3,6 litros é {numero_galoes36:,.2f} e o custo total é de R$ {valor_gasto36:,.2f}".replace(",","-").replace(".",",").replace("-","."))
print(resto18)
print(resto36)
salario_hora = float(input("Insira o seu pagamento por hora trabalhada: R$ "))
horas_trabalhadas_mes = float(input("Insira o total de horas trabalhadas no mês: "))
salario_bruto = salario_hora * horas_trabalhadas_mes
salario_liquido = salario_bruto - ((salario_bruto * 0.11) + (salario_bruto * 0.08) + (salario_bruto * 0.05))
if salario_bruto or horas_trabalhadas_mes != 0:
    print(f"a) O seu SALÁRIO BRUTO é R$ {salario_bruto:,.2F}".replace(".","-").replace(",",".").replace("-",","))
    print(f"b) O desconto de INSS é R$ {salario_bruto*0.11:,.2F}".replace(".","-").replace(",",".").replace("-",","))
    print(f"c) O IR descontado é R$ {salario_bruto*0.08:,.2F}".replace(".","-").replace(",",".").replace("-",","))
    print(f"d) O desconto do SINDICATO é R$ {salario_bruto*0.05:,.2F}".replace(".","-").replace(",",".").replace("-",","))
    print(f"e) O seu SALÁRIO LÍQUIDO é R$ {salario_liquido:,.2F}".replace(".","-").replace(",",".").replace("-",","))
else:
    print("O pagamento por hora ou as horas trabalhadas no mês não podem ser menor do que 0!")
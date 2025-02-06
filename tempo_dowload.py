print("O programa irá informar o tempo aproximado de download de um arquivo usando um determinado link.")
tamanho_arquivo = float(input("Informe o tamanho do arquivo em MB: "))
velocidade_link = float(input("Informe a velocidade do Link em Mbps: "))
print(f"O tempo aproximado de download em minutos é de {(tamanho_arquivo*8)/(velocidade_link):.2f} segundos ou {((tamanho_arquivo*8)/(velocidade_link))/60:.2f} minutos ")
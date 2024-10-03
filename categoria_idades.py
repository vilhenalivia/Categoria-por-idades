#Entrada do usuário
idade_indicada = int(input("\nDigite sua idade: "))

#Condicional de classificação das idades
if idade_indicada <= 12:
    print("\nVocê é classificado como: Criança.\n")
elif idade_indicada >= 13 and idade_indicada < 18:
    print("\nVocê é classificado como: Adolescente.\n")
elif idade_indicada >= 18:
    print("\nVocê é classificado como: Adulto.\n")
else:
    print("\nDigite uma resposta válida.\n")

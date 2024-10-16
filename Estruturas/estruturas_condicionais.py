Maior_idade = 18
Idade_Especial = 12

idade = int(input("Informe sua idade: "))
18

#primeira maneira
if idade >= Maior_idade:
    print("Maior de idade, pode tirar a CNH.")
if idade < Maior_idade:
    print("Não pode tirar a CNH.")

#outra maneira
if idade >= Maior_idade:
     print("Maior de idade, pode tirar a CNH.")
else:
    print("Não pode tirar a CNH.")

#verificacao idade
if idade >= Maior_idade:
     print("Maior de idade, pode tirar a CNH.")
elif idade == Idade_Especial:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas.")
else:
    print("Não pode tirar a CNH.")
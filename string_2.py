nome = "Ludmila"
idade = 23
profissao = "programador"
linguagem = "python"
saldo= 45.55
dados = {"nome": "Ludmila", "idade": 23}


print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(idade, nome))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome = nome, idade = idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age = idade, name= nome))
print("Nome: {nome} Idade: {idade}".format(**dados))#contatenando
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
    
salario = 2000

def salario_bonus(bonus):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")


    salario += bonus
    return salario
#iten imutavel
lista = [1]

novo_salario = salario_bonus(500) #2500
print(novo_salario)
print(lista)

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Ola mundo!")


print(calcular_total([10,20,34]))#64
print(retorna_antecessor_e_sucessor(10)) #(9 , 11)
print(func_3()) #se deixar o retorno em branco, o return vai ser none

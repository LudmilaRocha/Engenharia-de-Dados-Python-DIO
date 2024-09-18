
#pega um texto e separa as vogais desse texto, for percorre um objeti

texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
        if letra.upper() in VOGAIS:
            print(letra, end = "")
else:
      
        print()
        print("Executa o final do laço")
#exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
       print(numero, end="")
       
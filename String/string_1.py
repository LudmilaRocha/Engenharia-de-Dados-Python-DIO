#trabalhando strings e metodos

nome = "Ludmila"

#metodo para deixar tudo em maiusculo
print(nome.upper())
#metodo para deixar tudo em minusculo
print(nome.lower())
#metodo para deixar a primeira letra em maiscula e o resto em minuscula
print(nome.title())


texto = "  Olá Mundo!   "

#com espaço
print(texto + ".")
#sem espaço
print(texto.strip() + ".")
#cortar o espaço individualmente
#direita
print(texto.rstrip() + ".")
#esquerda
print(texto.lstrip() + ".")


menu = "Python"
#alinhamento de palavras para menus por exemplo (centralizar)
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(20, "#"))
print("P-y-t-h-o-n")


#exemplo
for letra in menu:
    print(letra, end= "-")
    print()
#forma de voce colocar um simbolo (traço) em cada letra
print("-".join)
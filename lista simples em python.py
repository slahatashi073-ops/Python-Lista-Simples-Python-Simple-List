import pprint


lista = []
print("O que você deseja adicionar na lista?")
item = input()
lista.append(item)
print(lista)

print("Você deseja adicionar mais um item na lista? (s/n)")
resposta = input()
if resposta == "s":
    print("O que você deseja adicionar na lista?")
    item = input()
    lista.append(item)
    print(lista)
    print("Obrigado por usar o programa!")
if resposta == "n":
    print(lista)
    print("Obrigado por usar o programa!")
else: print("Resposta inválida!")

print("você gostaria de reiniciar o programa? (s/n)")
resposta = input()
if resposta == "s":
        print(lista)
        print("Obrigado por usar o programa!")
        loop = True
if resposta == "n":
        loop = False
        print(lista)
        print("Obrigado por usar o programa!")
else: print("Resposta inválida!")

if loop == True:
    while True:
        print("O que você deseja adicionar na lista?")
        item = input()
        lista.append(item)
        print(lista)
        print("Você quer adicionar algo a mais na lista? (s/n)")
        resposta = input()
        if resposta == "s":
            print("O que você deseja adicionar na lista?")
            item = input()
            lista.append(item)
            print(lista)
        if resposta == "n":
            print("Obrigado por usar o programa!")
            break
if loop == False:
    print(lista)
    print("Obrigado por usar o programa!")
                                        #obrigado por ler!# #thanks for reading!#


for i in range(10):
    print(i)

dicionario = {"chave1": "valor1", "chave2":"valor2","chave3":"valor3"}

for i in dicionario:
    if i !=  "chave2":
        if i == "chave3":
            break
        print(dicionario[i])

indice = 0
a = dicionario.keys()[indice]

while a != "chave3":
    print(dicionario[a])
    indice +=1
    print(indice)
    a = dicionario.keys()[indice]
    print(a)


def xo(s):
    countX = None
    countO = None


    for i in range(len(s)):

        if (s.upper()[i]) == 'O':
            countO+=1
        elif (s.upper()[i]) == 'X':
            countX += 1


    return countO==countX
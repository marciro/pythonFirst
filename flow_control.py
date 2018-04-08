firstDictionary = {"chave1": "teste", "chave": 1980, "chave3": [0, 1, 2]}
firstList = ["0", "1", "2", "4"]
a = 1

if firstDictionary.has_key("chave2"):
    print("Entrou no primeiro if")
    print(firstDictionary.get("chave2"))
    b = 2
    print(a)
    print(b)
elif len(firstList) >= 4:
    print ("Entrou no segundo if")
    print (firstList[0])
    print(a)
    b = 5
    print(b)
else:
    print ("So o else mesmo")

print(b)



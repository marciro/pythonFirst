#Dicionarios sao como maps no Java ou Records


people1 = {"nome": "Marcelo Cicero",
          "idade": 37,
          "skills":['java','python','javascript']}

people2 = {"nome": "Fernanda",
          "idade": 36,
          "skills":['analise de materiais','solda','termodinamica']}

peoples = {"p1":people1,"p2":people2}
peoplesList = [people1,people2]
print(people1.get('nome'))

print(people1.fromkeys(["nome","skills"]
                      ))

print(people1.has_key("idade"))

print(people2.items())
print(peoples.items())
print(peoplesList[1])
from random import randrange


# names = ["Kraków", "Łódź", "Poznań", "Warszawa", "Wrocław", "Toruń", "Gdańsk", "Szczecin"]

# for _ in range(20):
#     fr = names[randrange(8)]
#     to = names[randrange(8)]
#     if fr != to:
#         print("{\"from\": \""+fr+"\", \"to\":\""+to+"\",\"weigth\": 100, \"price\": 100},")

# import confLoader


# cities, packages, parameters = confLoader.confLoader("config/conf2.json")

# counter = 1
# for i in packages:
#     for j in packages[i]:
#         waigth = randrange(100, 500)
#         road = 400
#         if j['to'] in cities[i]:
#             road = cities[i][j['to']]
#         price = waigth*3 + road*3 + randrange(-500, 500)
#         # print(i, "to", j['to'],waigth, price)

#         print("{\"id\": "+str(counter)+",\"from\": \""+i+"\", \"to\":\""+j['to']+"\",\"weigth\": "+str(waigth)+", \"price\": "+str(price)+"},")

#         counter+=1

from random import randrange


names = ["Kraków", "Łódź", "Poznań", "Warszawa", "Wrocław", "Toruń", "Gdańsk", "Szczecin"]

for _ in range(20):
    fr = names[randrange(8)]
    to = names[randrange(8)]
    if fr != to:
        print("{\"from\": \""+fr+"\", \"to\":\""+to+"\",\"weigth\": 100, \"price\": 100},")

import confLoader
from startPopGen import generateFirstPopulation

cities, packages, parameters = confLoader.confLoader("config/conf3.json")
generateFirstPopulation(cities, packages, parameters)
# packagesNumber = [x["id"] for x in packages.get("Kraków")]
# print(packagesNumber)
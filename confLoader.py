import json


def confLoader(path):
    
    cities = {}
    packages = {}
    parameters = {}
    with open(path, encoding="UTF-8") as json_file:
        data = json.load(json_file)
        parameters = data["parameters"]

        

        for city in data['cities']:
            cities[city["name"]] = {}
            for connection in city["connections"]:
                cities[city["name"]][connection["name"]] = connection["length"]
        
        for package in data['packages']:
            if package["from"] in packages:
                packages[package["from"]].append(package)
            else:
                packages[package["from"]] = [package]
            


    # print(cities)
    # print(packages)
    # print(packages)
    return cities, packages, parameters
    
animals = [   
     {"name": "capybara", "group": "mammal", "weight": 110},   
     {"name": "hedgehog", "group": "mammal", "weight": 0.5},    
     {"name": "bearded dragon", "group": "reptile", "weight": 1},    
     {"name": "tortoise", "group": "reptile", "weight": 40},   
     {"name": "hummingbird", "group": "bird", "weight": 0.01},    
     {"name": "elephant", "group": "mammal", "weight": 10000},    
     {"name": "ostrich", "group": "bird", "weight": 280},    
     {"name": "python", "group": "reptile", "weight": 180},    
     {"name": "blue whale", "group": "mammal", "weight": 300000},    
     {"name": "lion", "group": "mammal", "weight": 350}]

#Code to print the names of all animals that are heavier than 100lbs 
print("The following animals weigh more than 100lbs:  ")
for a in animals:
    if a["weight"] > 100:
        print(a["name"])

#code to print out the heaviest animal
heaviest = animals[0]
for a in animals:
    if a["weight"] > heaviest["weight"]:
        heaviest = a
print(f'The {heaviest["name"]} is the heaviest animal in the list')

#code to print out the heaviest animal
lightest = animals[0]
for a in animals:
    if a["weight"] < lightest["weight"]:
        lightest = a
print(f'The {lightest["name"]} is the lightest animal in the list')

#code to print out all the mammals in a list
mammals = []
print('This is the list of mammals in the list')
for a in animals:
    if a["group"] == "mammal":
        mammals.append(a)
print(mammals)

#code to find mammals with more than 7 letters in its name
long_named_animals = []
print("The following animals have more than 7 letters in its name")
for long_name in mammals:
    if(len(long_name["name"]) > 7):
        long_named_animals.append(long_name)
print(long_named_animals)

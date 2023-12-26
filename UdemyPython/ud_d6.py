from pathlib import Path
import os , glob

# Get the current working directory as a Path Object
folder = os.getcwd()
location = Path(folder)

# Get the number of recipes in the folder path
recipe_count = 0
for txt in location.glob('**/*.txt'):
    recipe_count += 1
 
name = input("Hello what's your name : ")
print(f"\n Hi,{name} welcome to Sefe's recipe book,\n you are currently in the \" {location} \" \n there are currently \" {recipe_count} \" recipes in my book")
print("\n Find below all our options and choose one")

reci_dic = {'1':"Read Recipe", '2':"Create Recipe", '3':"Create Category", '4':"Delete Category", '5':"Delete Category",'6':"End program"}
for key,values in reci_dic.items():
    print(key,values)
   
reply = input("Choose an option (1-6): ")
game_over = False

# Specify the subdirectory name
subdirectory_name = "Recipes"
categories = location / subdirectory_name

# # List all recipes in the "Recipes" directory
# print("\nList of Recipes:")
# for recipe_path in categories.glob('**/*.txt'):
#     print(recipe_path.name)

# def readRecipe():
#     print("You have choosen the Read Recipe option")
#     cateName = input("What Category would you like to view: ")
#     recName = input("Which recipe do you want to read? ")
#     recipe_path = categories / cateName / f"{recName}.txt"
#     with open(str(recipe_path), 'r') as file:
#         content = file.read()
#         print(content)
    

if reply == '1':
    print("You have choosen the Read Recipe option")

    # List all categories in the "Recipes" directory
    print("\nList of Categories:")
    for cate_path in categories.iterdir():
        print(cate_path.name)

    cateName = input("What Category would you like to view: ") 
    categ_path = categories / cateName
    if not cate_path.is_dir():
        print(f"Category '{cateName}' does not exist.")
    else:
        #  choose recipe
        for inRecName in categ_path.iterdir():
            print(inRecName)
        recName = input("Which recipe do you want to read? ")
#   read recipe    
    recipe_path = cate_path / f"{recName}.txt"
    if recipe_path.is_file():
        with open(str(recipe_path), 'r') as file:
            content = file.read()
            print(content)
    else:
        print(f"The specified recipe '{recName}' in category '{cateName}' does not exist.")

#     go back to menu
#     pass
elif reply == '2':
    print("You have choosen the Create Recipe in a specific category option")
#  List all categories in the "Recipes" directory
    print("\nList of Categories:")
    for cate_path in categories:
        print(cate_path.name)
#   #choose category
    cateName = input("What Category would you like to view: ")
    recipe_path = categories / cateName 
#   #create new recipe file
    recName = input("What would you like to name this recipe: ")
    recContent = input("Your recipe: ")
    new_file_path = os.path.join(recipe_path,recName)
    with open(new_file_path, 'w') as new_file:
        new_file.write(recContent)
#     #go back to menu
#     pass
# elif reply == 3:
#     #create category
#     #go back to menu
#     pass
# elif reply == 4:
#     #show categories
#     #choose category
#     #show recipes
#     #choose recipe
#     #eliminate recipe
#     #go back to menu
#     pass
# elif reply == 5:
#     #show categories
#     #choose category
#     #eliminate category
#     #go back to menu
#     pass
# else:
#     game_over = True

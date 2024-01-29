from pathlib import Path
from os import system
import os , glob

# Get the current working directory as a Path Object
folder = os.getcwd()
location = Path(folder)


    # Get the number of recipes in the folder path
def count_recipes(path):
    recipe_count = 0
    for txt in Path(path).glob('**/*.txt'):
        recipe_count += 1

    return recipe_count

def start():
    system('cls')
    print('*' * 50)
    name = input("Hello what's your name : ")
    print(f"\n Hi, {name} welcome to Sefe's recipe book,\n ou are currently in the \" {location} \" \n There are currently \" {count_recipes(location)} \" recipes in my book")
    print("\n Find below all our options and choose one")
    print('*' * 50)

    reply = 'x'
    while not reply.isnumeric() or int(reply) not in range(1,7):
        reci_dic = {'1':"Read Recipe", '2':"Create Recipe", '3':"Create Category", '4':"Delete Category", '5':"Delete Category",'6':"End program"}
        for key,values in reci_dic.items():
            print(key,values)
        reply = input("Choose an option (1-6): ")

    return int(reply)

def show_categories(path):
    print("Categories: ")
    cate_path = Path(path)
    cate_list = []
    counter = 1

    #  List all categories in the "Recipes" directory
    print("\nList of Categories:")
    for folder in cate_path.iterdir():
        folder_str = str(folder.name)
        print(cate_path.name)
        print(f"[{counter}] - {folder_str}")
        cate_list.append(folder)
        counter += 1
    return cate_list

def choose_categories(a_list):
    correct_choice = 'x'
    while not correct_choice.isnumeric() or int(correct_choice) not in range (1, len(a_list) + 1):
        correct_choice = input("\n Choose a category: ")

    return a_list[int(correct_choice)-1]

def show_recipes(path):
    print("These are the recipes: ")
    recipes_path = Path(path)
    recipes_list = []
    counter = 1

    for recipe in recipes_path.glob('*.txt'):
        recipe_str = str(recipe.name)
        print(f"[{counter}] - {recipe_str}")
        recipes_list.append(recipe)
        counter += 1
    return recipes_list

def choose_recipes(a_list):
    recipe_choice = 'x'
    
    while not recipe_choice.isnumeric() or int(recipe_choice) not in range(1, len(a_list) + 1):
        recipe_choice = input("\n Choose a recipe: ") 
    return a_list[int(recipe_choice)]

def read_recipe(recipe):
    print(Path.read_text(recipe))

def create_recipe(path):
    exists = False

    while not exists:
        print("Write the name of your recipe: ")
        recipe_name = input() + '.txt'
        print("Write your new recipe here:")
        recipe_content = input()
        new_path = Path(path, recipe_name)

        if not os.path.exists(new_path):
            Path.write_text(new_path, recipe_content)
            print(f"Your recipe {recipe_name} has been created")
            exists = True
        else:
            print("Sorry, this already exists ")

def create_category(path):
    exists = False
    while not exists:
        print("Write the name of your category: ")
        cate_name = input() 
        new_path = Path(path, cate_name)

        if not os.path.exists(new_path):
            Path.mkdir(new_path)
            print(f"Your new category {cate_name} has been created")
            exists = True
        else:
            print("Sorry, this already exists ")

def delete_recipe(recipe):
    Path(recipe).unlink()
    print(f"The recipe {recipe.name} has been deleted")

def del_cate(category):
    Path(category).rmdir()
    print(f"The Category {category.name} has been deleted")

def return_beginning():
    return_choice = 'x'

    while return_choice.lower() != 'b':
        return_choice = input("\n Press b to return to the begining: ")

game_over = False

while not game_over:
    reply = start()
    if reply == 1:
        print("You have choosen the Read Recipe option")
        my_categories = show_categories(location)
        my_cate_variable = choose_categories(my_categories)
        my_recipe = choose_recipes(my_cate_variable)
        read_recipe(my_recipe)
        return_beginning()
    elif reply == 2:
        print("You have choosen the Create Recipe in a specific category option")
        my_categories = show_categories(location)
        my_cate_variable = choose_categories(my_categories)
        my_recipe = show_recipes(my_cate_variable)
        create_recipe(my_cate_variable)
        return_beginning()
    elif reply == 3:
        create_category(location)
        return_beginning()
    elif reply == 4:
        print("You have choosen the Read Recipe option")
        my_categories = show_categories(location)
        my_cate_variable = choose_categories(my_categories)
        my_recipe = show_recipes(my_cate_variable)
        my_recipe = choose_recipes(my_cate_variable)
        delete_recipe(my_recipe)
        return_beginning()
    elif reply == 5:
        print("You have choosen the Read Recipe option")
        my_categories = show_categories(location)
        my_cate_variable = choose_categories(my_categories)
        del_cate(my_cate_variable)
        return_beginning()
    else:
        game_over = True
    
    start()

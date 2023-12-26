#A Simple program to determine the amount of commission workers earned
name = input("What is your name: ")
sales = int(input("How many sales did you make this period "))
comission = round(((sales * 13)/100),2)

print(f"The amount of comission that {name} earned for selling {sales} is {comission}")
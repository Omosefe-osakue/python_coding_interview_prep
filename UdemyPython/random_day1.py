# #Code to check if a number is even or odd (using a fixed variable)

# var = 12
# var2 = 11

# if (var2 % 2 == 0):
#     {print("This ", var2, " is even")}
# else:
#     {print("This " , var2," is odd")}
    
# #Code to check if a number is even or odd (using a list of variables)
# li = [1,2,5,6,7,8,9]
# i = 0
# for i in li:
#     if (i % 2 == 0):
#         {
#             print("This ", i, " is even")
#         }
#     else:
#          {print("This " , i," is odd")}
#     i = i + 1
    
# #Code to check if a number is even or odd (using a list of variables ad add to specific lists)
# li = [1,2,5,6,7,8,9,16,19,23,25,27,29,30,32,50,56,100,91]
# leven = []
# lodd = []
# i = 0
# for i in li:
#     if (i % 2 == 0):
#         {
#             leven.append(i)
#         }
#     else:
#          {
#              lodd.append(i)
#          }
#     i = i + 1
    
# print("The following values are even ",leven)
# print("The following values are odd ",lodd)

# #Code to check if a number is even or odd (using a inputted variable)
# num = float(input("Please enter a number: "))
# if (num % 2 == 0):
#     {print("This ", num, " is even")}
# else:
#     {print("This " , num," is odd")}
    
# #Code to check if a number is even or odd (using a inputted list of variable)(Revisit)
# num = []
# num2 = []
# i = 0
# li_num = int(input("How many numbers would you be adding to your list: "))
# while i < li_num:
#     num1 = float(input("Please enter a number: "))
#     num2 = num.append(num1)
#     i += 1
# print(num2)

# #Code to check if a number is a palindrome

n = 12344321
k = 0
i = 0
j = -1
li = []

for i in n:
    li.append(i)
   

if (len(n)%2 == 0):
     while (k < len(n)//2):
         if(li[i] == li[j]):
             i = i + 1
             j = j - 1
         else:
             break
# else:
#     {print("The number ", n, " is not a plaindrome")}

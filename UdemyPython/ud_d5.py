import random
#A bunch of practical examples

#Challenge 1
#a function that returns a value in the function
#based on the sum value 
# def return_distincts(a,b,c):
#     sum1 = a + b + c
#     lists1 = [a,b,c]
  
#     for i in lists1:
#         if(sum1>15):
#             print(max(lists1))
#             return max(lists1)
#         elif sum1<10:
#             print(min(lists1))
#             return min(lists1)
#         else:
#            lists1.sort()
#            print(lists1[1])
#            return lists1[1]

# return_distincts(2,4,7)

#Challenge 2
# A function that takes a word and returns only its unique letters
# def word_set(word):
#     list1 = []
#     mySet = set()
#     for i in word:
#          mySet.add(i)
    
#     list1 = list(mySet)
#     list1.sort()
#     print(list1)
#     return list1

# word_set("sefe")

#Challenge 
#A function that returns a boolean value depending 
#on the positioning of the zeros
# def neighboring_zeros(*args):
#     counter = 0
#     for arg in args:
#         if counter +1 ==len(args):
#             return False
#         elif args[counter] == 0 and args[counter+1] == 0:
#             return True
#         else:
#             counter += 1
#     return False

# print(neighboring_zeros(4,6,64,0,3,5,2,2,0))
        
        
#The Hangman Game
#Made use of the Udemy course tutorial
words = ["time","dashes","letter","valid"]
correct_letters=[]
incorrect_letters = []
tries = 6
right_answers = 0
game_over = False

def word_choice(word_list):
    random_words = random.choice(word_list)
    different_letters = len(set(random_words))
    return random_words, different_letters

def ask_letter():
    chosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    while not is_valid:
        chosen_letter = input("Please choose a letter : ")
        
        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You haven't chosen a letter")
            
    return chosen_letter

def show_new_board(random_words):
    
    hidden_list = []
    
    for l in random_words:
        if l in correct_letters:
            hidden_list.append(l)
        else:
            hidden_list.append('-')
            
    print(' '.join(hidden_list))
    
def check_letter(chosen_letter,hidden_word, tries, matches):
    end = False
    if chosen_letter in hidden_word and chosen_letter not in correct_letters:
        correct_letters.append(chosen_letter)
        matches += 1
    elif chosen_letter in hidden_word and chosen_letter in correct_letters:
        print("You have found this letter before. Try again")
    else:
        incorrect_letters.append(chosen_letter)
        tries -= 1
        
    if tries == 0:
        end = lose()
    elif matches  == unique_letters:
        end  = win(hidden_word)
        
    return tries, end, matches

def lose():
    print("You don't have any tries left")
    print("The hidden word was "+ word)
    
    return True

def win(revealed_word):
    show_new_board(revealed_word)
    print("Congratulations, you guessed the word!!!")
    
    return True

word, unique_letters = word_choice(words)
while not game_over:
    print('\n' + '*' * 20 + '\n')
    show_new_board(word)
    print('\n')
    print('incorrect letters: ' + '-'.join(incorrect_letters))
    print(f'Tries: {tries}')
    print('\n' + '*' * 20 + '\n')
    letter = ask_letter()
    tries,over,right_answers = check_letter(letter,word,tries, right_answers)
    game_over = over
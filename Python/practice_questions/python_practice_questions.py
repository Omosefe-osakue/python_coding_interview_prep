"""
    Author : Omosefe Osakue
    Date : 11-February-2024
    Some Practice Coding questions I came across when trying to master python for interviews

"""

# code to reverse a string
s = "help"
rs = s[::-1]
print(rs)


# code to check if a given string is a palindrome
def check_palindrome(word):
    rs_word = word[::-1]
    if word == rs_word:
        print(f"{word} is a palindrome")
        return True
    else:
        print(f"{word} is not a palindrome")
        return False


check_palindrome("sefe")
check_palindrome("abba")


# Find the factorial
def factorial(n):
    fact = 1
    if n < 0:
        print("This is a negative number, we can't find the factorial for this")
    elif n == 0:
        print(1)
    else:
        for i in range(1, n + 1):
            fact = fact * i
        print(fact)


factorial(1)
factorial(10)
factorial(0)
factorial(-1)


# fibanocci series
def fibonacci(n):
    fib = [0, 1]

    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    print(fib)
    return fib


fibonacci(7)


# function to calculate the number of numerical digits in a string
def digit(word):
    count = 0
    for i in word:
        if i.isdigit():
            count += 1
        else:
            pass
    print(count)


digit("he24hk56bb7866htnkg9u9565ki5985u54nt")


# function to find the count for the occurrence of a particular character in a string
def occurence(word):
    count = 0
    for i in word:
        if i == "a":
            count += 1
        else:
            continue
    print(count)


# print(word.count("a"))

occurence("abababafjkdsjnafsdna")


# find the non-matching characters in a string
def non_matching_characters(str1, str2):
    non_matchching_array = []
    min_len = min(len(str1), len(str2))

    # check if values are the same
    for i in range(min_len):
        if str1[i] != str2[i]:
            non_matchching_array.append((str1[i], str2[i]))
    if len(str1) > len(str2):
        for i in range(min_len, len(str1)):
            non_matchching_array.append((str1[i], None))
    if len(str1) < len(str2):

        for i in range(min_len, len(str2)):
            non_matchching_array.append((None, str2[i]))

    print(non_matchching_array)


non_matching_characters("Sefe", "Safe")


# to find out if the two given strings are anagrams
def check_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    print(sorted(str1) == sorted(str2))


check_anagrams("sefe", "safe")
check_anagrams("abab", "baba")


# calculate the number of vowels and consonants in a string?
def alaphabet_calculator(word):
    vowel_count = 0
    consonant_count = 0

    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowel_count += 1
        else:
            consonant_count += 1
    print(vowel_count, consonant_count)


alaphabet_calculator("occurrence")


# total all of the matching integer elements in an array
def matching_integer(word_list):
    matching_list = {}
    total = 0

    for elements in word_list:
        if elements in matching_list:
            matching_list[elements] += 1
        else:
            matching_list[elements] = 1

        for elements, count in matching_list.items():
            if count > 1:
                total += elements * count

    print(total)


matching_integer([45, 45, 5, 6, 3, 4, 5, 6, 3])


def reverse_array(ar):
    print(ar[::-1])


arr = [1, 2, 3, 4, 5]
reverse_array(arr)


# to find the max element in an array
def find_max_element(ar):
    max_elem = ar[0]

    for i in ar:
        if i > max_elem:
            max_elem = i

    print(max_elem)


find_max_element([1, 2, 3, 46, 7, 8, 90, 65, 3, 2, 2])


# to sort an array of integers in ascending order
def sorted_array(arr):
    sorted_arr = sorted(arr)
    print(sorted_arr)


sorted_array([1, 2, 3, 46, 7, 8, 90, 65, 3, 2, 2])


# to print a Fibonacci sequence using recursion
def fibonacci(num):
    fib_seq = [0, 1]
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        while len(fib_seq) < num:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])

        return fib_seq


ans = fibonacci(3)
ant = fibonacci(7)
print(ans)
print(ant)


# to calculate the sum of 2 integers
def int_sum(num1, num2):
    print(num1 + num2)


int_sum(2, 8)


# to find average of numbers in a list
def average_list(arr):
    noOfElem = len(arr)
    sumOfElem = sum(arr)

    mean = sumOfElem / noOfElem
    print(mean)


average_list([2, 3, 56, 6, 8, 4, 3, 6])


# to check if an integer is even or odd
def checkdigit(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


checkdigit(7)
checkdigit(13456789)
checkdigit(5678)


# to reverse an integer in python
def reverse_int(num):
    print(str(num)[::-1])


reverse_int(7894)


# to determine if a num is an armstrong
def is_armstrong(num):
    sum = 0
    for i in str(num):
        sum += int(i) ** 3
    if sum == num:
        print(f"{num} is an Armstrong Number")
    else:
        print(f"{num} is not an armstrong number")


is_armstrong(34)
is_armstrong(153)
is_armstrong(370)


# program to check if a number is a prime or not
def is_prime(num):
    count = 0

    for i in range(2, num // 2):
        if num % i == 0:
            count = 1
            break
    if count == 1:
        print("This is not a prime number")
    else:
        print("This is a prime number")


is_prime(2)
is_prime(12)
is_prime(13)
is_prime(234)
is_prime(4355)


# program to find the fibanocci series
def fib_seq(n):
    fib = [0, 1]

    if n <= 0:
        print("Can't find the fibonacci for negative numbers")
    elif n == 1:
        print([0])
    else:
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        print(fib)


fib_seq(10)
fib_seq(5)
fib_seq(2)
fib_seq(-4)

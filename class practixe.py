#Python Program to Check Whether a Given Number is Even or Odd using Recursion
'''def is_even(number):
    # base case
    if number == 0:
        return True
    # recursive case for even numbers
    elif number > 0:
        return is_odd(number - 1)
    # recursive case for odd numbers
    else:
        return is_odd(number + 1)

def is_odd(number):
    # base case
    if number == 1:
        return True
    # recursive case for odd numbers
    elif number > 1:
        return is_even(number - 1)
    # recursive case for even numbers
    else:
        return is_even(number + 1)

# test the function
num = int(input("Enter a number: "))
if is_even(num):
    print(num, "is even")
else:
    print(num, "is odd")'''
#Python Program to Check Whether a Number is Positive or Negative

'''num = float(input("Enter a number: "))
if num > 0:
    print(num, "is positive")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is negative")'''

#Python Program to Check if a Number is a Palindrome

'''def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")'''

#Python Program to Reverse a Number

'''num = int(input("Enter a number: "))
rev_num = 0
while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num = num // 10
print("The reversed number is:", rev_num)'''

#Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

'''for i in range(1, 101):
    if i % 2 != 0 and i % 3 != 0:
        print(i)'''
#Python Program to Find Sum of Digit of a Number Without Recursion

'''num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("The sum of the digits is:", sum)'''

#Python Program to Print Table of a Given Number

'''num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)'''

#Python Program to Read a Number n and Compute n+nn+nnn

'''n = int(input("Enter a number: "))
nn = n * 11
nnn = n * 111
result = n + nn + nnn
print("n + nn + nnn =", result)'''

#Python Program to Check if a Number is a Strong Number

'''def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += factorial(digit)
    temp //= 10

if num == sum:
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")'''


#Python Program to Print Numbers in a Range Without using Loops

'''def print_range(start, end):
    if start <= end:
        print(start)
        print_range(start+1, end)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print_range(start, end)'''

#Python Program to Check If Two Numbers are Amicable Numbers or Not

'''def proper_divisors_sum(n):
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if proper_divisors_sum(num1) == num2 and proper_divisors_sum(num2) == num1:
    print(num1, "and", num2, "are amicable numbers")
else:
    print(num1, "and", num2, "are not amicable numbers")'''

#Python Program to Find Whether a Number is a Power of Two

'''def is_power_of_two(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

num = int(input("Enter a number: "))

if is_power_of_two(num):
    print(num, "is a power of two")
else:
    print(num, "is not a power of two")'''

#Python Program to Find Product of Two Numbers using Recursion

'''def product(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    elif num2 > 0:
        return num1 + product(num1, num2-1)
    else:
        return -product(num1, -num2)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Product of", num1, "and", num2, "is", product(num1, num2))'''

#Python Program to Find All Perfect Squares in the Given Range

'''import math

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Perfect squares in the range [", start, ",", end, "]:")
for i in range(start, end+1):
    if math.sqrt(i) == int(math.sqrt(i)):
        print(i)'''
#Python Program to Print All Possible Combinations of Three Digits

'''for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i != j and j != k and k != i:
                print(i, j, k)'''
#Python Program to Find Fibonacci Numbers using Recursion

'''def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter the number of Fibonacci numbers to generate: "))

print("The first", num, "Fibonacci numbers are:")
for i in range(num):
    print(fibonacci(i))'''

#Python Program to Find the Fibonacci Series Without using Recursion

'''num = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci = [0, 1]
for i in range(2, num):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print("The first", num, "Fibonacci numbers are:")
for i in range(num):
    print(fibonacci[i])'''

#Python Program to Find the Factorial of a Number using Recursion

'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a non-negative integer to find its factorial: "))

if num < 0:
    print("Error: Please enter a non-negative integer.")
else:
    print("The factorial of", num, "is", factorial(num))'''

#Python Program to Find the Factorial of a Number Without Recursion

'''num = int(input("Enter a non-negative integer to find its factorial: "))

if num < 0:
    print("Error: Please enter a non-negative integer.")
else:
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    print("The factorial of", num, "is", factorial)'''
#Python Program to Check if a String is a Pangram or Not

'''import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(sentence.lower())

sentence = input("Enter a sentence: ")

if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")'''

#Python Program to Remove Odd Indexed Characters in a string

'''def remove_odd_index_chars(string):
    return string[::2]

string = input("Enter a string: ")

new_string = remove_odd_index_chars(string)

print("The new string with odd indexed characters removed is:", new_string)'''

#Python Program to Remove the nth Index Character from a Non-Empty String

'''def remove_nth_char(string, n):
    return string[:n] + string[n+1:]

string = input("Enter a string: ")
n = int(input("Enter the index of the character to remove: "))

new_string = remove_nth_char(string, n)

print("The new string with the nth index character removed is:", new_string)'''

#Python Program to Replace All Occurrences of ‘a’ with $ in a String

'''def replace_chars(string):
    return string.replace('a', '$')

string = input("Enter a string: ")

new_string = replace_chars(string)

print("The new string with 'a' replaced with '$' is:", new_string)'''

#Python Program to Replace Every Blank Space with Hyphen in a String

'''def replace_spaces(string):
    return string.replace(' ', '-')

string = input("Enter a string: ")

new_string = replace_spaces(string)

print("The new string with spaces replaced with hyphens is:", new_string)'''

#Python Program to Reverse a String Without using Recursion

'''def reverse_string(string):
    return string[::-1]

string = input("Enter a string: ")

new_string = reverse_string(string)

print("The reversed string is:", new_string)'''


#Python Program to Find Common Characters in Two Strings

'''def common_characters(string1, string2):
    common = ""
    for char in string1:
        if char in string2 and char not in common:
            common += char
    return common

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

common = common_characters(string1, string2)

print("The common characters in the two strings are:", common)'''

#Python Program to Find the Larger String without using Built-in Functions

'''def string_length(string):
    count = 0
    for char in string:
        count += 1
    return count

def find_larger_string(string1, string2):
    length1 = string_length(string1)
    length2 = string_length(string2)
    if length1 > length2:
        return string1
    elif length2 > length1:
        return string2
    else:
        return "The two strings have the same length."

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

larger_string = find_larger_string(string1, string2)

print("The larger string is:", larger_string)'''

#Python Program to Check if a Given String is Palindrome

'''def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

string = input("Enter a string: ")

if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")'''

#Python Program to Check whether a String is Palindrome or not using Recursion

'''def is_palindrome(string):
    if len(string) < 2:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])

string = input("Enter a string: ")

if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")'''

#Python Program to Add a Key-Value Pair to the Dictionary

'''my_dict = {"apple": 3, "banana": 5, "cherry": 2}

print("Original dictionary:")
print(my_dict)

key = input("Enter a key: ")
value = int(input("Enter a value: "))

my_dict[key] = value

print("Updated dictionary:")
print(my_dict)'''

#Python Program to Create a Class which Performs Basic Calculator Operations


'''class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

# example usage
calc = Calculator()
print("Addition: ", calc.add(2, 3))
print("Subtraction: ", calc.subtract(10, 7))
print("Multiplication: ", calc.multiply(3, 4))
print("Division: ", calc.divide(15, 5))'''























    


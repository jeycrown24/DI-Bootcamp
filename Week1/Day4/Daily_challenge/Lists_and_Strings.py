#Challenge 1: Multiples of a Number
#
#Instructions:
#1. Ask the user for two inputs:
#A number (integer).
#A length (integer).
#2. Create a program that generates a list of multiples of the given number.
#3. The list should stop when it reaches the length specified by the user.

user_number = int(input("Please input a number: "))
user_length = int(input("Please input a length: "))
numbers = []
for i in range (1, user_length+1):
    numbers.append(user_number * i)
print (numbers)

#Challenge 2: Remove Consecutive Duplicate Letters
#
#Instructions:
#1. Ask the user for a string.
#2. Write a program that processes the string to remove consecutive duplicate letters.
#The new string should only contain unique consecutive letters.
#For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
#3. The program should print the modified string.

user_word = input("Please input a word: ")
result = list(user_word)
new_result = []
for char in result:
    if not new_result:
        new_result.append(char)
    elif char != new_result[-1]:
        new_result.append(char)
print("".join(new_result))
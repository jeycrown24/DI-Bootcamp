#Exercise 1: Favorite Numbers
#
#Instructions:
#
#Create a set called my_fav_numbers and populate it with your favorite numbers.
#Add two new numbers to the set.
#Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {7,8,24,42,72}
my_fav_numbers.add(27)
my_fav_numbers.add(787)
my_fav_numbers.remove(787)
friend_fav_numbers = {1,4,23,54,69}
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)

#Exercise 2: Tuple
#
#Instructions:
#
#Given a tuple of integers, try to add more integers to the tuple.
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

numbers = (1, 2, 3, 4, 5)
#Tuples are immutable, so you cannot add more integers to the tuple after it has been created. You would need to create a new tuple if you want to include additional integers.
new_numbers = numbers + (6, 7, 8)
print(new_numbers)

#Exercise 3: List Manipulation
#
#Instructions:
#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
#Remove "Blueberries" from the list.
#Add "Kiwi" to the end of the list.
#Add "Apples" to the beginning of the list.
#Count how many times "Apples" appear in the list.
#Empty the list.
#Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apples_count = basket.count("Apples")
print(f"Apples count is: {apples_count}")
basket.clear()
print(basket)

#Exercise 4: Floats
#
#Instructions:
#Recap: What is a float? What’s the difference between a float and an integer?
#Create a list containing the following sequence of mixed types: floats and integers:
#1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
#Avoid hard-coding each number manually.
#Think: Can you generate this sequence using a loop or another method?
#
# Float is a data type that represents numbers with decimal points, while an integer is a whole number without any decimal points. The main difference is that floats can represent fractional values, whereas integers cannot.
numbers_mixed = [_ + 0.5 for _ in range(1, 5)] + [_ for _ in range(2, 6)]
numbers_mixed.sort()
print(numbers_mixed)

#Exercise 5: For Loop
#
#Instructions:
#Write a for loop to print all numbers from 1 to 20, inclusive.
#Write another for loop that prints every number from 1 to 20 where the index is even.
for i in range(1, 21):
    print(i)
for index,number in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(number)

#Exercise 6: While Loop
#
#Instructions:
#Use an input to ask the user to enter their name.
#Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
#hint: check for the method isdigit()
#if the input is incorrect, keep asking for the correct input until it is correct
#if the input is correct print “thank you” and break the loop

while True:
    name = input("Enter your name: ")
    if len(name)<3 or any(char.isdigit() for char in name):
        print ("Invalid input. Please try again.")
    else:
        print("Thank you")
        break

#Exercise 7: Favorite Fruits
#
#Instructions:
#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
#Store these fruits in a list.
#Ask the user to input the name of any fruit.
#If the fruit is in their list of favorite fruits, print:
#"You chose one of your favorite fruits! Enjoy!"
#If not, print:
#"You chose a new fruit. I hope you enjoy it!"

input_fruits=input("Enter your favorite fruits: ")
favorite_fruits = (input_fruits).split()
print(favorite_fruits)
fruit=input("Enter the name of any fruit: ")
if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#Exercise 8: Pizza Toppings
#
#Instructions:
#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types 'quit'.
#For each topping entered, print:
#"Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.

toppings = []
while True:
    topping = input("Enter a topping (or type 'quit' to finish): ")
    if topping == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
total_cost = 10 + 2.5*len(toppings)
toppings_text = ", ".join(toppings)
print(f"Your toppings: {toppings_text}")
print(f"Total cost of the pizza: ${total_cost:.2f}")

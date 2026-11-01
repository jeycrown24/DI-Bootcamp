#Exercise 1: Converting Lists into Dictionaries
#
#Instructions
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
user_dict=(dict(zip(keys,values)))
print (user_dict)

#Exercise 2: Cinemax #2
#Instructions
#Write a program that calculates the total cost of movie tickets for a family based on their ages.
#Family members’ ages are stored in a dictionary.
#The ticket pricing rules are as follows:
#Under 3 years old: Free
#3 to 12 years old: $10
#Over 12 years old: $15

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
cost=0
for name, age in family.items():
    if age <3:
        ticket_price = 0
    elif 3<=age<=12:
        ticket_price = 10
    else:
        ticket_price = 15
    print(f"{name},{ticket_price}$")
    cost += ticket_price
print(f"Total cost is: {cost}$")
#Bonus:
#Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family_new = {}
while True:
    name_new = input("Please enter a name: ")
    if name_new == "done":
        break
    age_new = int(input("Please enter an age: "))
    family_new [name_new] = age_new
cost_new = 0
for name_new, age_new in family_new.items():
    if age_new <3:
        ticket_price = 0
    elif 3<=age_new<=12:
        ticket_price = 10
    else:
        ticket_price = 15
    print(f"{name_new} {ticket_price}$")
    cost_new += ticket_price
print(f"Total cost is: {cost_new}$")

#Exercise 3: Zara
#
#Instructions
#name: Zara
#creation_date: 1975
#creator_name: Amancio Ortega Gaona
#type_of_clothes: men, women, children, home
#international_competitors: Gap, H&M, Benetton
#number_stores: 7000
#major_color: 
#    France: blue, 
#    Spain: red, 
#    US: pink, green
#
#Create and manipulate a dictionary that contains information about the Zara brand.
#Create a dictionary called brand with the provided data.
#Modify and access the dictionary as follows:
#Change the value of number_stores to 2.
#Print a sentence describing Zara’s clients using the type_of_clothes key.
#Add a new key country_creation with the value Spain.
#Check if international_competitors exists and, if so, add “Desigual” to the list.
#Delete the creation_date key.
#Print the last item in international_competitors.
#Print the major colors in the US.
#Print the number of keys in the dictionary.
#Print all keys of the dictionary.

brand = {"name":"Zara","creation_date":1975,"creator_name":"Amancio Ortega Gaona","type_of_clothes":["men","women","children","home"],"international_competitors":["Gap","H&M","Benetton"],"number_stores":7000, "major_color":{
    "France":"blue",
    "Spain":"red",
    "US":["pink","green"]
}}
brand["number_stores"]=2
print(f"Zara has huge variety of clothes for everyone: {', '.join(brand['type_of_clothes'])}")
brand["country_creation"]="Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
brand.pop("creation_date")
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand.keys()))
print(brand.keys())

#Bonus:
#Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

more_on_zara={"creation_date":1975,"number_stores":7000}
more_on_zara = brand | more_on_zara
print (more_on_zara)

#Exercise 4: Disney Characters
#
#Instructions
#You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
#Character List:
#users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#Expected Results:
#1. Create a dictionary that maps characters to their indices:
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#2. Create a dictionary that maps indices to characters:
#{0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
#{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
users_1={}
for index, user in enumerate(users):
    users_1 [user] = index
print (users_1)
users_2={}
for index, user in enumerate(users):
    users_2 [index] = user
print (users_2)
users_3={}
sorted_users=sorted(users)
for index, user in enumerate(sorted_users):
    users_3 [user] = index
print (users_3)

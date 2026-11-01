#Daily challege: Build up a string
#
#Instructions:
#1. Ask for User Input:
#The string must be exactly 10 characters long.
#2. Check the Length of the String:
#If the string is less than 10 characters, print: "String not long enough."
#If the string is more than 10 characters, print: "String too long."
#If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
#3. Print the First and Last Characters:
#Once the string is validated, print the first and last characters.
#4. Build the String Character by Character:
#Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.
#5. Bonus: Jumble the String (Optional)
#As a bonus, try shuffling the characters in the string and print the newly jumbled string.


sent = input ("Please insert a string: ")
if len(sent) <10:
    print ("String not long enough.")
elif len(sent) >10:
    print ("String too long.")
else:
    print("Perfect string.")
    print(sent[0])
    print(sent[-1])
    result = ""
    for char in sent:
        result += char
        print (result)
    import random 
    letters = list(sent)
    random.shuffle(letters)
    shuffled = "".join(letters)
    print (f"Shuffled verison: {shuffled}")
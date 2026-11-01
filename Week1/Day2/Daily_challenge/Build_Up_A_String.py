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
import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728

list_of_numbers_1=[]
for i in list_of_numbers:
    if i <= target_number:
        list_of_numbers_1.append(i)

found_pairs=[]

for a in list_of_numbers_1:
    for b in list_of_numbers_1:
        pair=(a,b)
        if a==b and list_of_numbers_1.count(a)<2:
            continue
        if a+b==target_number and a<=b and pair not in (found_pairs):
            found_pairs.append(pair)
            print (f"{pair} sums to the target_number {target_number}")
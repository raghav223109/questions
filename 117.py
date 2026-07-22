#count how many time each vowel occurs in a day 

text = input("enter your string :")
vowels = {}
for i in text:
    if i in "aeiouAEIOU":
        if i in vowels:
            vowels[i] = vowels[i]+1
        else:
            vowels[i] = 1
#print(vowels)

for key,value in vowels.items():
    print(f"{key} : {value}")
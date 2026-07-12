s = input("enter your string:")

def vowel(s):
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count

print(vowel(s))
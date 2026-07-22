# reverse the word if the given string 

text = input("enter the string:")
result = ""
word = text.split()
word.reverse()
result = " ".join(word) 
print(result)
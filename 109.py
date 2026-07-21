# convert string to title case without using title()

text = input("enter a string: ")
words = text.split()

title = ""
for word in words:
    title += word[0].upper() + word[1:].lower() + " "

print(title)
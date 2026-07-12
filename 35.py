string = "apple"
freq = {}

for ch in string:
    freq[ch] = freq.get(ch,0)+1
print(freq )
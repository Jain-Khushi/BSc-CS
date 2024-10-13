string =  input('Enter the string : ')
freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
maxFreq = max(freq, key = freq.get)
print(maxFreq , "is the maximum frequency character with frequency of " , freq[maxFreq])

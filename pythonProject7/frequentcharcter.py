
# Getting string input from the user
myStr =  input('Enter the string : ')

# Finding the maximum frequency character of the string
freq = {}
for i in myStr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
maxFreqChar = max(freq, key = freq.get)

# Printing values
print("Entered String is ", myStr)
print(maxFreqChar , "is the maximum frequency character with frequency of " , freq[maxFreqChar])

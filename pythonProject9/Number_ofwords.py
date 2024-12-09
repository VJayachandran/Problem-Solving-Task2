
string = ("Enter the string:")  #print the string
char=0
word=1
for i in string:
      char=char+1              #counts the characters in words
      if(i==' '):
            word=word+1        #Counts the words
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)
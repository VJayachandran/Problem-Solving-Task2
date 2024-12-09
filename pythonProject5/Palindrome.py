
str_1 = input ("Enter the string to check if it is palindrome:")
str_1 = str_1.casefold()
rev_str= reversed (str_1)     #checking the string from reverse

if list(str_1) == list(rev_str):   #checking the strings list with reversed string list

       print("The String is a Palindrome")
else:
       print("The string is not a Palindrome")



myStr="Python For Beginners"
print("The input string is:",myStr)   # print the string
output=[]
for character in myStr:
    if character not in output:       #checking the if condition
        output.append(character)      # this method used to concatenate strings together
print("The output is:",output)        # prints the output removing the unique character
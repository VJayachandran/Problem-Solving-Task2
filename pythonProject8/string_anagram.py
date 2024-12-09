# Declare Inputs
inp1 = "listen"
inp2 = "silent"

# Sort Elements
x = [inp1[i] for i in range(0, len(inp1))]
x.sort()
y = [inp2[i] for i in range(0, len(inp2))]
y.sort()

# the sorted strings are checked
if (x == y):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")

## Example 2 for "The strings aren't anagrams."

# Declare Inputs
inp1 = "listen"
inp2 = "silenti"

# Sort Elements
x = [inp1[i] for i in range(0, len(inp1))]
x.sort()
y = [inp2[i] for i in range(0, len(inp2))]
y.sort()

# the sorted strings are checked
if (x == y):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")
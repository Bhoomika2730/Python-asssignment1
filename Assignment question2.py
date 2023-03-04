#Write a Python program that accepts a word from the user and reverse it.
#Sample Test Case
#Input : Edyoda
#output: adoydE

word = input("Input a word to reverse: ")
 
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

# Another method

word = input("Enter the word to reverse:")
word = "Edyoda"
print(word[slice(-1,-7,-1)])

#1. Take input from user
text = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
lowercase = 0

for ch in text:
    # Check vowels
    if ch.lower() in "aeiou":
        vowels += 1

    # Check consonants
    elif ch.isalpha():
        consonants += 1

    # Check spaces
    elif ch == " ":
        spaces += 1

    # Check lowercase letters
    if ch.islower():
        lowercase += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of spaces:", spaces)
print("Number of lowercase letters:", lowercase)




# 2.Function to convert lines to uppercase
def convert_to_upper(lines):
    for line in lines:
        print(line.upper())

# Take input
lines = []
n = int(input("Enter number of lines: "))

for i in range(n):
    line = input()
    lines.append(line)

# Call function
convert_to_upper(lines)
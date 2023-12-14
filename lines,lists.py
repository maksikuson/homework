#Part 1

#Task 1

def palindrome(i):
    i = i.replace(" ", "").lower()
    return i == i[::-1]

line = input("Enter line: ")
if palindrome(line):
    print("It's a palindrome!")
else:
    print("This is not a palindrome(.")


with open ('file1.txt', 'w+',encoding='utf-8') as file1:
    file1.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur auctor efficitur eleifend. Praesent lacinia orci dui, non bibendum libero fermentum a.")
with open ('file2.txt', 'w+',encoding='utf-8') as file2:
    file2.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur auctor efficitur eleifend. Phasellus nisl arcu, laoreet vitae justo sit amet, feugiat commodo nulla. ")
#Task 1
file1_path = "file1.txt"
file2_path = "file2.txt"

with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
     lines1 = file1.readlines()
     lines2 = file2.readlines()

differences1 = [line for line in lines1 if line not in lines2]
differences2 = [line for line in lines2 if line not in lines1]

if differences1:
    print(f"Lines that do not match in {file1_path}:\n{differences1}")
else:
    print(f"All lines in {file1_path} match.")
    
if differences2:
    print(f"Lines that do not match in {file2_path}:\n{differences2}")
else:
    print(f"All lines in {file2_path} match.")
    
#Task 2

with open('file1.txt', 'r',encoding='utf-8') as file1:
    numberOfFiles = file1.read()
    symbol = len(numberOfFiles)
    lines = len(numberOfFiles.splitlines())
    
    vomels = 'aeiou'
    vomelsCount = sum(char.lower() in vomels for char in numberOfFiles)
    
    consonants = 'bcdfghjklmnpqrstvwxyz'
    consonantCount = sum(char.lower() in consonants for char in numberOfFiles)
    
    digits = sum(char.isdigit() for char in numberOfFiles)
    

print(f"Number of symbols: {symbol}")
print(f"Number of lines: {lines}")
print(f"Number of vowels: {vomelsCount}")
print(f"Number of consonant letters: {consonantCount}")
print(f"Number of digits: {digits}")

#Task 3

input_file_path = "file1.txt"
output_file_path = "file2.txt"

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()
    
if lines:
    lines.pop()
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(lines)
else:
    print("The file is empty or missing.")
    
print(f"The last line was deleted and the result was written to the file: {output_file_path}")

#Task 4

input_file_path = "file1.txt"

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()
    
if lines:
    max_length = max(len(line) for line in lines[:2])   
     
    print(f"The length of the longest line among the first two: {max_length}")
else:
    print("The file is empty or missing.")
    
#Task 5

wordUser = input("Enter word: ")

with open('file1.txt', 'r', encoding='utf-8') as file1:
    numberOfFiles = file1.read()
    
count = numberOfFiles.lower().split().count(wordUser.lower())

print(f"Word {wordUser} occurs in the file {count} times")

#Task 6

with open('file1.txt', 'r', encoding='utf-8') as file1:
    numberOfFiles = file1.read()

wordDelite = input("Enter word to delite: ")
wordNew = input("Enter new word: ")
updateFile = numberOfFiles.replace(wordDelite,wordNew)

with open('file1.txt', 'r', encoding='utf-8') as file1:
    file.write(updateFile)
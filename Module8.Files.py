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

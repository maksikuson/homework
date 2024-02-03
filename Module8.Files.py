file_path = "file1.txt"
file2_path = "file2.txt"

with open(file_path, 'r', encoding='uth-8') as file1, open(file2_path, 'r', encoding='uth-8') as file2:
     lines1 = file1.readlines()
     lines2 = file2.readlines()
     

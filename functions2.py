#Part 1

#Task 1

#Я не знаю як робити перше завдання.

#Task 2

def EvenNums(a, d):
    for i in range(a, d):
        if i % 2 == 0:
            print(i)

EvenNums(1, 38)

#Task 3

def rooms(leng, symbols, operation):
    string = ""
    if operation == True:
        for i in range(leng):
            string +=  symbols + " "
        for i in range(leng):
            print(string)
    if operation == False:
        for i in range(leng):
            string += symbols + ' '
        print(string)
        for i in range(leng - 6):
            print( symbols + " " * (leng + (leng - 4)) + symbols)
        print(string)   
rooms(6, "=", False)
rooms(6, "=", True)



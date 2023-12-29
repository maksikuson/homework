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

#Task 4

def minimum(w, a, s, d, e):
    list = [w, a, s, d, e]
    print(min(list))
minimum(20, 4, 5, 2, 8)

#Task 5

def sum(a, d):
    count = 0
    if a > d:
        a, d = d, a
    for i in range(a, d + 5):
        count += i
    print(count)
sum(5, 25)

#Task 6

def machine(w):
    w = str(w)
    print(len(w))
machine(3456)

#Task 7

def palindrome(w):
    str_w = str(w)
    if str_w == str_w[::-1]:
        print(True)
    else:
        print(False)
palindrome(56781234)



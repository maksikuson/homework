#Part 2

#Task 1

def machine(list):
    result = 1
    for i in list:
        result *= i
    return result
print(machine([2, 4, 6, 8]))

#Task 2

def minimum(list):
    result = min(list)
    return result
print(minimum([2, 4, 6, 8]))

#Task 3

def numbers(num):
    if num <2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
        return True
def lists(list1):
     count = 0
     for i in list1:
         if numbers(i):
             count +=1
     return count
list2 = [2,3,4,5,10,11,12,13]
result = lists(list2)
print(f"The number of prime numbers in the list: {result}")

#Task 4

def lens(num, list1):
    list1 = list(list1)
    list1.remove(num)
    return list1

print(lens(4, [2, 3, 4, 5, 6]))

#Task 5

def lens(a, d):
    result = a + d
    return result
print(lens([1, 2, 3, 4], [5, 6, 7, 8]))

#Task 6

def lens(num, list):
    result = ""
    for i in list:
        i = i ** num
        i = str(i) + " "
        result += i
    return result

print(lens(4, [1, 2, 3, 4, 5]))
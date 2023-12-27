#Part 2

#Task 1

# numbers = input('Enter arithmetic expression (for example "23 + 12"): ')
# print(eval(numbers))

#Task 2

# import random
 
# list = [random.randint(-100,100) for i in range(10)]
# print(list)
# print(f'max: {max(list)}, min: {min(list)}')
# count_less_zero = 0
# for i in range(len(list)):
#     if list[i] < 0:
#       count_less_zero += 1
# print(f'number of negative numbers :{count_less_zero}')
# count_more_zero = 0
# for i in range(len(list)):
#     if list[i] > 0:
#        count_more_zero += 1
# print(f'number of positive numbers :{count_more_zero}')
# count_zero = 0
# for i in range(len(list)):
#     if list[i] == 0:
#        count_more_zero += 1
# print(f'number of numbers equal to zero :{count_zero}')

#Part 3

#Task 1

# import random

# list1 = [random.randint(0, 20) for i in range(5)]
# list2 = [random.randint(0, 20) for i in range(5)]
# print(list1)
# print(list2)
# merged_list = list1 + list2
# print(merged_list)
# merged_list_no_repetiton = list(set(merged_list))
# print(merged_list_no_repetiton)
# merged_list_no_repetiton_2 = list(set(list1) & set(list2))
# print(merged_list_no_repetiton_2)
# unique_elements_list1 = list(set(list1) - set(list2))
# unique_elements_list2 = list(set(list2) - set(list1))
# unique_elements = unique_elements_list1 + unique_elements_list2
# print(unique_elements)
# min_max_list = [min(list1), max(list1), min(list2), max(list2)]
# print(min_max_list)
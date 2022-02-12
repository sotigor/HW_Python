import random
# Homework_for_lesson_6

# Task_1. Finding the greatest number in the list.

# Creating a list of random numbers
list_of_numb = []
counter = 0
while counter < 10:
    random_number = random.randint(1, 100)
    list_of_numb.append(random_number)
    counter += 1

# Find the max value in the list
index_of_numb = 0
max_value = list_of_numb[0]
while index_of_numb < len(list_of_numb)-1:
    if list_of_numb[index_of_numb] > max_value:
        max_value = list_of_numb[index_of_numb]
    index_of_numb += 1
print(f'The max value in the list {list_of_numb} is: {max_value}')

# Task_2. Making a list which contains the common numbers of two another lists without duplicates.

# Creating two lists with random numbers
list_1 = []
list_2 = []
counter = 0
while counter < 10:
    random_number_1 = random.randint(1, 10)
    random_number_2 = random.randint(1, 10)
    list_1.append(random_number_1)
    list_2.append(random_number_2)
    counter += 1

# Making a list which contains the common numbers of above two lists without duplicates

list_com = []
n = 0
while n < 10:
    if list_1[n] in list_2 and list_1[n] not in list_com:
        list_com.append(list_1[n])
    if list_2[n] in list_1 and list_2[n] not in list_com:
        list_com.append(list_2[n])
    n += 1
print(f'The list of common elements from lists \n{list_1} and {list_2} is: {list_com}')

# Task_3. Creating a list with integers which divisible by 7 but not a multiple of 5

cons_list = list(range(1,101))
counter = 0
new_list = []
while counter < len(cons_list)-1:
    if cons_list[counter] % 7 == 0 and cons_list[counter] % 5 != 0:
        new_list.append(cons_list[counter])
    counter += 1
print(f'The list where each element divisible by 7 but not a multiple of 5 is: {new_list}')

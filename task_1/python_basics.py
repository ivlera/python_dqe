'''
Create a python script:

create list of 100 random numbers from 0 to 1000
sort list from min to max (without using sort())
calculate average for even and odd numbers
print both average result in console
'''

import random


# 1. Creating list of random numbers

# Creating empty list to store random numbers
rand_list = []

# Iteration from 0 to 100 is required to produce exactly 100 values
for i in range(100):
    # Producing random value via 'randint' function from previously imported 'random' module and inserting this value into list
    rand_list.append(
        random.randint(0, 1000)
    )

# 2. Bubble sort implementation

# Creating a variable that stores integer value that is equal to the amount of items in previously created list - this is required for further iteration
rand_list_len = len(rand_list)

# Creating a flag and setting it to True - this is required in order to start 'while loop' and finish it when all numbers in list will be sorted
already_sorted = True
while already_sorted: # further loop will be executing only if 'already_sorted' flag is set to True
    # Setting flag to False - if further 'if' condition will be False, then 'already_sorted' flag will become equal to False and this condition will exit 'while loop'
    already_sorted = False
    # Iterating through indexes in list, in current example iteration will go from 0 to 99
    for i in range(rand_list_len - 1):
        # Following condition checks whether current number is bigger then number next to it
        # e.g. on the first iteration if list starts from [1, 2,...] then following condition won't be executed
        # on the first iteration if list starts from [2, 1,..] then following condition will be executed
        if rand_list[i] > rand_list[i + 1]:
            # Values will change order, e.g. [2, 1,..] will become [1, 2,...]
            rand_list[i], rand_list[i + 1] = rand_list[i + 1], rand_list[i]
            # Setting flag to True, so 'while loop' won't stop execution and iteration will be moved to the next items
            # e.g. if list is equal to [1, 2, 3, ...] after first iteration, variable 'i' will become = 1 and next items to check the line 40 condition will be 2 and 3
            already_sorted = True
    # In case if after all iterations condition on line 40 was always False, it means that list is already sorted and 'already_sorted' flag will become equal to False(line 34) and while loop will stop execution

# 3. Calculate average for even and odd numbers

# Creating two empty lists where further will be stored even and odd numbers
odds = []
evens = []

# Iterating through list
for i in rand_list:
    # If value on the current iteration can be divided by 2 without remainder then this value is even
    if i % 2 == 0:
        # Adding even value to the list of evens
        evens.append(i)
    # If value on the current iteration can't be divided by 2 without remainder then this value is odd
    else:
        # Adding odd value to the list of odds
        odds.append(i)

# Calculating average value by dividing sum of values by amount of values in list
odds_avg = sum(odds)/len(odds)
evens_avg = sum(evens)/len(evens)

# 4. Print both average result in console
print(odds_avg)
print(evens_avg)

'''
Write a code, which will:

1. create a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

2. get previously generated list of dicts and create one common dict:
if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
'''

import random
import string


# 1. Create a list of random number of dicts (from 2 to 10)

# Creating empty list where dictionaries will be stored
dict_list = []
# Iterating through random range of numbers via 'random' module, this will allow to create from 2 to 10 dictionaries
for l in range(random.randint(2, 10)):
    # Empty dict where keys and values will be stored
    dict_list_item = {}
    # As in above iteration, using 'random' to create from 2 to 10 key-value pairs
    for i in range(random.randint(2, 10)):
        # Assigning key and pair that will be added to 'dict_list_item' dict
        # Key = random lowercase letter that is created via 'string' module and chosen up randomly via 'random' module
        # Value = random number from 0 to 100
        dict_list_item[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
    # After iteration finished execution, we have from 2 to 10 key-value pairs in 'dict_list_item' dict and appending this dict into 'dict_list' list
    dict_list.append(dict_list_item)
dict_list = [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. Get previously generated list of dicts and create one common dict:

# Creating empty dict where key-value pairs will be stored
dict_common = {}

# Creating empty list where will be stored all keys from each dict
# this is required to verify either item is unique within all dictionaries or it has several occurrence
dict_list_keys = []
# Iterating through each dict by index
for i in range(len(dict_list)):
    # Collecting all keys from dict on current iteration via keys() method
    # Adding list of keys into 'dict_list_keys'; using extend() in order to have plain list, not nested
    dict_list_keys.extend(dict_list[i].keys())

# Iterating through each dict by index
for i in range(len(dict_list)):
    # Iterating through each key-value in dict
    for k, v in dict_list[i].items():
        # Check whether item is unique (has one occurrence through all dicts in list) by using count() method on 'dict_list_keys' list of keys
        if dict_list_keys.count(k) == 1:
            # If value is 'unique' - adding it to the dictionary
            dict_common[k] = v
        # If value occurred more than once in all dicts in list then adding key-value pair where key is changed
        else:
            # Changing key - adding underscore and index+1 to it; +1 here is needed cause indexes starting from 0, not 1
            # Value remains unchanged
            dict_common[f'{k}_{i+1}'] = v

# Empty dict where keys that are repeated more than once and have the biggest value will be stored
repeatable_item_max = {}
# Iterating through each key-value in dict
for k, v in dict_common.items():
    # Check whether key is longer than 1 symbol
    # Keys that are longer than 1 symbol are the ones where '_{index+1}' was added during previous steps - these keys needs to be deleted in case they have lower value in comparison to other keys that have same letter
    if len(k) > 1:
        # Check whether letter in current iteration already exists in 'repeatable_item_max' dict
        if k[0] in repeatable_item_max.keys():
            # If letter exists, then check whether it's value is bigger than the one that was added before
            if v > repeatable_item_max[k[0]]:
                # if value is bigger - than just replacing value with bigger one
                repeatable_item_max[k[0]] = v
        # If such letter (key) doesn't exist in dict, then adding key and value from current iteration
        else:
            repeatable_item_max[k[0]] = v

# Creating empty dict where will be added unique key-value pairs and keys having MAX values in case if key was repeated in initial list of dicts
dict_common_final = {}
for k, v in dict_common.items():
    # Check key length in order to verify if it was unique or it is the one that was repeated but has max value
    if len(k) > 1:
        # Check whether key letter in current iteration already exists in 'repeatable_item_max' dict
        if k[0] in repeatable_item_max.keys():
            # If key letter is in 'repeatable_item_max' dict, then need to check whether its value is biggest, i.e. if it same as value in 'repeatable_item_max'
            if v == repeatable_item_max[k[0]]:
                # If value in current iteration is same as value for same key letter in 'repeatable_item_max' dict, than this is the one that should be added to the final dict
                # Adding key-value pair without changing the key, cause key is already represented as, for example, 'a_1'
                dict_common_final[k] = v
    # Above condition won't be executed in case if key-value pair was unique in very first list of dicts
    # Adding such key-value pairs to the final dict additional checks
    else:
        dict_common_final[k] = v

print(dict_common_final)

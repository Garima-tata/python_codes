
'''
#'immutable'
Tuples - ()
Sets - {}
'''

my_list = [1,23,4,5,565]
my_list[1] = 100
print(my_list)

# TUPLES

my_tuple = (1,2,3,4)
# my_tuple[1] = 1000 "can't assign as it is immutable"

# SET
my_set = {22,22,1,2,3,4,5,5,5,5,5,'tiger','tiger','tiger'}
print(my_set)
my_set.add("garima")
print(my_set)







# DICTIONARY
'''
- Basic dictionaries
- Accessing a value
- Accessing all key:value pairs
- Printing all values
- Changing a value
- Adding a key:value pair
- Removing a key:value pair
'''
my_dict = {'John':30,'Anna':29,'Fiona':29}
my_dict['Anna']

for pair in my_dict:
    print(pair)
    
# dict[Key] == Value
for pair in my_dict:
    print(my_dict[pair])

# adding key value pair
my_dict['John'] = 31
print(my_dict)

my_dict['Phil'] = 26
print(my_dict)

my_dict.pop('Phil')
print(my_dict)
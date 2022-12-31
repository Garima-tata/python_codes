#Executing code a certain number of times
count = 10
for blahh in range(10):
    count*=5
    print(blahh)
    print("Count: {}".format(count))
    '''
    Code to train our algorithm
    '''
#Iterating through datasets (e.g. lists)
my_list = [1,2,3,4,5,6]
my_string = "Hi there I like python"

for element in my_list:
    element +=100
    print('Element value: {}'.format(element))

# break
fruit_list = ['apple','pear','bannana','moldy bannana','kiwi']
[5,6,7,8,8,55]
for fruit in fruit_list:
    if fruit == 'moldy bannana':
        break
    else:
        print(fruit)
print('Production stopped. Moldy bannana found!')

# continue
fruit_list = ['apple','pear','bannana','moldy bannana','kiwi']
[5,6,7,8,8,55]
for fruit in fruit_list:
    if fruit == 'moldy bannana':
        continue
    else:
        print(fruit)
print('Production stopped. Moldy bannana is skipped!')
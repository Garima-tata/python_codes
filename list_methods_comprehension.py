'''
List methods:
- append
- remove
- pop
- sort
- reverse
List functions:
- len()
- min()
- max()
'''
myList = [1,4,56,7777,44,22]
myListLetters = ['a','g','z','f','b']
myList.reverse()
print(myList)

myList.sort()
print(myList)

myList.append(4)
print(myList)

myList.remove(7777)
print(myList)

myList.pop()
print(myList)

myList.pop(3)
print(myList)

a=min(myListLetters)
b=max(myListLetters)
c=len(myListLetters)
print(a,b,c)


# list Indexing

list=[["garima","divyanshu","tanmay","Banwari","lalita"],900,55,34,32,"Anmol","Asmit","Chinmay","BL"]
print(list[0][4])
print(list[3])
print(list[3:8])
print(list[:5])
print(list[5::2])
print(list[::4])
print(list[:])

# list in list
linl=[9,6,5,["hi","hello",["bye","sayonara","tata","alvida"],"namaste","kemcho"],3,8,3,6,7]

print(linl[3][:2])
print(linl[3][2][1:])
print(linl[::-1])


# list comprehension
'''
-Quick way to create new lists
- Quick way to create new lists with conditions (if x%2==0)
- Means to filter through a list with new condition
'''

a=11%2
my_list = [i for i in range(100)]
print(my_list)

my_odd_list = [number for number in range(15) if number%5!=0]
print(my_odd_list)

fruit_list = ['apple','pear','kiwi','bannana','moldy bannana']
fresh_fruit_list = [fruit for fruit in fruit_list if fruit != "moldy bannana"]
print(fresh_fruit_list)

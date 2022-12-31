import random
# Random Guess Programm using while
'''g=random.randint(1,100)
x=True
while (x==True):
    n=int(input())
    if (n==g):
        x=False
    elif (n>g):
        print("your number is too big")
    else:
        print("your number is too low")'''
        
# Random Guess with max five lives
y=True
lives=5
while (lives>0):
    r=random.randint(0,1)
    n=int(input("enter a guess"))
    if (n==r):
        print("yayy, you Won")
    elif (n>r):
        lives=lives-1
        print(f"you are left with only {lives} lives")
    else:
        lives=lives-1
        print(f"you are left with only {lives} lives")
    

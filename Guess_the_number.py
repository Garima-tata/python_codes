import random
# Random Guess
m=random.randint(1,100)
n=int(input())
if (m>n):
    print("Your Guess is too small")
elif(m<n):
    print("your Guess is too Big")
else:
    print("Correct Guess !!!!!")


# Twister
colors=["Red","Yellow","Pink","Black"]
direction=["left Hand","right Hand","left Leg","right Leg"]

# r=colors[random.randint(0,3)]
# d=direction[random.randint(0,3)]

# OR
r=random.choice(colors)
d=random.choice(direction)

print("Twister spinner says {},{}".format(d,r))
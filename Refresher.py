# Basic Star Pattern
print("Star Pattern \n")
for i in range(1,20):
    for j in range (i) :
        print("*", end="")
    print()
# Inverted Star pattern
print("Inverted Star pattern\n")
for i in range (20,1,-1):
    for j in range (i,1,-1):
        print('*',end="")
    print('\n')
new_file= open("New_file.txt",'x')
new_file.close()
#check of a file exists

import os
print("Checking if my_file exists or nots.....")
if os.path.exists("my_file.txt"):
    os.remove ("my_file.txt")
else:
    print("The file doesn't exist")

my_file=open('my_file.txt','w')
my_file.write("You are lab experiment")
my_file.close()

os.remove('aa.txt')
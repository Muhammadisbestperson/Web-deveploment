file1 = open("E:/MBH/Codingal/Myfile.txt","r")
file2 = open("E:/MBH/Codingal/aa.txt","w")



for line in file1.readlines():


    if not (line.startswith('Coding')):
        print(line)
        file2.write(line)

#Close and Save the files

file2.close()
file1.close()
file_read = open ("E:/MBH/Codingal/Myfile.txt","r")
print('File in Read Mode-')
print(file_read.read())
file_read.close()
#open the file in write mode
file_write=open("E:/MBH/Codingal/Myfile.txt","w")
#write in the file

file_write.write("Big man in the suit of armor take that off What are you.")
file_write.close()
#open the file in append mode
file_append=open("E:/MBH/Codingal/Myfile.txt","a")
#append in the file

file_append.write("Billionare Playboy Philanthropist.")
file_append.close()
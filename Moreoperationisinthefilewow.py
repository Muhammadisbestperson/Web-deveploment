with open ('E:/MBH/Codingal/aa.txt','r') as file:
    data= file.readlines()
    print("Stark and Rogers talk together between the news lets see what are they saying")
    for line in data:
        word=line.split()
        print (word)
file.close()

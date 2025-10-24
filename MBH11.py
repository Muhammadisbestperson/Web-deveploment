import random
import time
def getRandomDate(startDate,endDate):
    print("Printing random date between ",startDate,"and", endDate)
    randomGenerator=random.random()
    dateformat='%m/%d/%Y'
    starttime=time.mktime(time.strptime(startDate,dateformat))
    end_time=time.mktime(time.strptime(endDate,dateformat))
    randomtime=starttime+end_time*(end_time-starttime)
    randomDate=time.strftime(dateformat,time.localtime(randomtime))
    return getRandomDate
print("Random Date=",getRandomDate("1/1/2024","10/28/2025"))
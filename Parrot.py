class Parrot:    
    species="Bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing  ".format(self.name)
blu=Parrot("Blu",10)
print(blu.sing("'Happy'"))
print (blu.dance())
woo=Parrot("Woo",15)
print("Blu is a {}".format(blu.species))  
print("Woo is also a {}".format(woo.species))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))
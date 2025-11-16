#class creation
class Dog:
    types="Protein"
    types2="Beaf"
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
Protein=Dog("Protein",5)
Beaf=Dog("Beaf",9)
print("A dog eats {} for a lunch".format (Protein.types))
print("A dog eats {} for dinner".format(Beaf.types2))
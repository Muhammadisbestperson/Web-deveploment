class Pakistan():
    def capital(self):
        print("Islamabad is the capital of Pakistan")
    def language(self):
        print("Urdu is spoken in most parts of Pakistan")
    def type(self):
        print("Pakistan is an agricultural country")
class UnitedStatesofAmerica():
    def capital(self):
        print("Washington D.C is the capital of United States")
    def language(self):
        print("American English is widely spoken in the United States")
    def type(self):
        print("America is dirty country")


obj_pak=Pakistan()
obj_usa=UnitedStatesofAmerica()

for country in(obj_pak,obj_usa):
    country.capital()
    country.language()
    country.type()
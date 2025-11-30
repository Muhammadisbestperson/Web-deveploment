class Ferrari:
    def mileage(self):
        print("The mileage of ferrari is 8.77 kmpl")
    def max_speed(self):
        print("The maximum speed of ferrari is 210km/h")
class BMW:
    def mileage(self):
        print("The milage of BMW is 47 kmpl ")
    def max_speed(self):
        print("the max speed of BMW is 305 km/h")
obj_ferr=Ferrari()
obj_bmw=BMW()

for vehicle in (obj_ferr,obj_bmw):
    vehicle.mileage()
    vehicle.max_speed()
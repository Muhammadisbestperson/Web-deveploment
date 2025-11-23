class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        self.name=name

class Bus (Vehicle):
    pass
School_bus= Bus("School Volvo",180,12)
print("Vehocle Name:",School_bus.name,"Speed:",School_bus.max_speed,"Mileage:",School_bus.mileage)
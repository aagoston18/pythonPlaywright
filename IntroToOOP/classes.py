#class names always strart with capital letters

class Vehicle:
    def __init__(self, brand, model, enginecc):
        self.brand = brand
        self.model = model
        self.enginecc = enginecc
        print("hi I'm your new car. I'm made by " +brand + ", I am of model: " + model + ", and my engine capacity is " + str(enginecc) + "cc")

veh1 = Vehicle("VW", "Golf ", 1599)
# print(veh1.brand)
# print(veh1.model)
# print(veh1.enginecc)

class Car:
    brand = 'Volvo'
    model = 'XC60'
    enginecc = 2499

#object of the class - an instantiation
car1 = Car

# print(car1.enginecc)
# print(car1.brand)
# print(car1.model)
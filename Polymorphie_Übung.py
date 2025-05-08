class Transportmittel:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        
    def show(self):
        return f'{self.name} ist ein Transportmittel.'
    
    def set_speed(self, speed):
        self.speed = speed
        return f'{self.name} bewegt sich mit einer Geschwindigkeit von {self.speed} km/h.'
    
class Auto(Transportmittel):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        
    def show(self):
        return f'{self.name} ist ein {self.color} Auto.'
    
class Bus(Transportmittel):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity
        
    def show(self):
        return f'{self.name} ist ein Bus mit einer Kapazität von {self.capacity} Passagieren.'
    
class Motorrad(Transportmittel):
    def __init__(self, name, type_):
        super().__init__(name)
        self.type_ = type_
        
    def show(self):
        return f'{self.name} ist ein {self.type_} Motorrad.'
    
##################################################################################
a = Auto('BMW', 'schwarz')
b = Bus('Mercedes', 50)
m = Motorrad('Harley', 'Cruiser')
print(a.show())
print(b.show())
print(m.show())
print(a.set_speed(120))

print(b.set_speed(80))
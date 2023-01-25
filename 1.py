class Car():
    """
    Автомобиль
    имеет цвет
    имеет мощность двигателя
    имеет максимальный запас бензина в баке
    имеет рассход (15 л на 100 км)
    """
    color: str = 'red'  # цвет
    power: int = 100  # мощность двигателя
    tank_capacity = 50  # объем бака
    fuel_consumption = 15  # расход топлива на 100 км
    fuel_now = 0  # топлива в баке сейчас

    def __init__(self,  color: str = 'red', power: int = 100, tank_capacity = 50, fuel_consumption = 15, fuel_now = 0):
        self.color = color
        self.power = power
        self.tank_capacity = tank_capacity
        self.fuel_consumption = fuel_consumption
        self.fuel_now = fuel_now

    def set_color(self):
        self.color = 'black'
        return self.color

    def get_fuel_now (self):
        return self.fuel_now

    def set_fuel_now(self):
        if self.fuel_now < 50 or self.fuel_now >=0:
            self.fuel_now += 25
            return self.fuel_now

    def get_engine_power(self):
        return self.power

    def get_fuel_consumption(self):
        self.fuel_consumption = self.fuel_now / self.fuel_consumption
        return self.fuel_consumption

BMV = Car()
BMV.set_color()
BMV.get_fuel_now()
BMV.set_fuel_now()
BMV.get_engine_power()
BMV.get_fuel_consumption()
print(BMV.set_color())
print(BMV.get_fuel_now())
print(BMV.set_fuel_now())
print(BMV.get_engine_power())
print(BMV.get_fuel_consumption())
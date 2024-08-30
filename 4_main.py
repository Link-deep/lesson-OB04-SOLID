# 2.3 Принцип разделения интерфейсов (ISP, Interface Segregation Principle)

# пример без использования данного принципа
class SmartHouse():
    def turn_on_light(self):
        pass
    def turn_off_light(self):
        pass
    def turn_on_tv(self):
        pass
    def turn_off_tv(self):
        pass
    def head_food(self):
        pass

# очень похоже на принцип S - единственной ответственности
# Пример имспралвения данного класса с использованием ISP

class Light():
    def turn_on_light(self):
        print("Свет включен")
    def turn_off_light(self):
        print("Свет выключен")

class TV():
    def turn_on_tv(self):
        print("ТВ включен")
    def turn_off_tv(self):
        print("ТВ выключен")

class Food():
    def head_food(self):
        print("Есть еда")





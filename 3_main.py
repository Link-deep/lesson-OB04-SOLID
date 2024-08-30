# Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)

# класс подстановки

class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying")


class Penguin(Bird):
    def fly(self):  # можно конечно переопределить класс, но если этого не делать, то мы
        # получим принт - Пингвин летает, что не верно и чтобы решить эту проблему
        # мы можем использовать принцип подстановки Барбары Лисков
        print("I can't fly")

penguin = Penguin("Penguin")
penguin.fly()

# Используем принцип Бабрары Лисков

class Bird_class():
    def fly(self):
        print("I fly")

class Duck_class():
    def fly(self):
        print("This is Duck fly fast")

def fly_in_the_sky(animal):
    animal.fly()

b = Bird_class()
d = Duck_class()

fly_in_the_sky(b)
fly_in_the_sky(d)


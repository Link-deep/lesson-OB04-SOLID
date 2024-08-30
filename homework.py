# Задача: Разработать простую игру, где игрок может использовать различные
# типы оружия для борьбы с монстрами. Программа должна быть спроектирована
# таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.


from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, damage):
        self.damage = damage

    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def __init__(self):
        super().__init__(damage=10)
    def attack(self, name, monster):
        print(f"{name} Axe attack with {self.damage} damage {monster.health}")
        health = monster.health - self.damage
        monster.health = health
        print(f"{monster.name} health {monster.health}")

class Gun(Weapon):
    def __init__(self):
        super().__init__(damage=20)
    def attack(self, name, monster):
        print(f"{name} Axe attack with {self.damage} damage")
        health = monster.health - self.damage
        monster.health = health
        print(f"{monster.name} health {monster.health}")

class Bow(Weapon):
    def __init__(self):
        super().__init__(damage=5)
    def attack(self, name, monster):
        print(f"{name} Axe attack with {self.damage} damage")
        health = monster.health - self.damage
        monster.health = health
        print(f"{monster.name} health {monster.health}")



class Fighter():
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

    def attack(self, monster):
        self.weapon.attack(self.name, monster)

class Monster():
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0


m = Monster('Monster', 30)
f = Fighter('IVAN', Sword())

# Основной игровой цикл
while m.is_alive():
    f.attack(m)  # IVAN атакует монстра
    if not m.is_alive():
        print("Monster is defeated! Game Over.")
        break

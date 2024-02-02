# CONSTRUCTOR


class Hero:  # Ini templatenya
    # __init__ itu adalah Inisialisasi
    # self ini adalah si hero1
    # si hero1 ini bisa digantikan dengan si self ini, didalam __init__
    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        self.name = inputName
        self.healt = inputHealth
        self.attack = inputAttack
        self.armor = inputArmor


hero1 = Hero("Yuna", "Healt : 1000", 500, 50)
hero2 = Hero("Fanny", "Healt : 200", 2000, 20)
hero3 = Hero("balmond", "Healt : 1000", 300, 500)

print(hero1.name)
print(hero2.healt)
print(hero3.attack)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

# print(hero1.name, hero1.healt, hero1.attack, hero1.armor)

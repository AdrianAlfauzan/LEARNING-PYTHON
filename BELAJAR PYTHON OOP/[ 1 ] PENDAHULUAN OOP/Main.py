class Hero:  # Ini templatenya
    pass


hero1 = Hero()  # Ini objectnya / instance (instantiation)
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "adrian"
hero3.health = 300

print(hero1)
print(hero1.__dict__)
# __dict__ --> ini berfungsi mengeluarkan semuanya
# Output --> {'name': 'sniper', 'health': 100} --> ini adalah atributnya
print(hero1.name)
# Output --> sniper --> objectnya

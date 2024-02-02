# CONSTRUCTOR


class Hero:  # Ini templatenya
    # Class variabel / static variabel
    jumlah = 0
    # jadi yang atas itu khusus untuk variabel
    # dan yang dibawah itu <def __init__()> itu khusus instancenya

    # __init__ itu adalah Inisialisasi
    # self ini adalah si hero1
    # si hero1 ini bisa digantikan dengan si self ini, didalam __init__
    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        # INI ADALAH INSTANCE VARIABLE
        # JADI NAME,HEALT,ATTACK,ARMOR --> AKAN DIMILIKI SI hero1,2,3 dll
        self.name = inputName
        self.healt = inputHealth
        self.attack = inputAttack
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Membuat Hero dengan nama" + inputName)


hero1 = Hero("Yuna", "Healt : 1000", 500, 50)
print(Hero.jumlah)
hero2 = Hero("Fanny", "Healt : 200", 2000, 20)
print(Hero.jumlah)
hero3 = Hero("balmond", "Healt : 1000", 300, 500)
print(Hero.jumlah)

# print(hero1.name)
# print(hero2.healt)
# print(hero3.attack)
print(Hero.__dict__)

# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)

# print(hero1.name, hero1.healt, hero1.attack, hero1.armor)

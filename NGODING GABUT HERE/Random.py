import random

user_input = input("Masukkan jawaban : ")
choices = ["ronaldo", "pessi", "neymar", "ramos"]
random_choice = random.choice(choices)


if user_input == random_choice:
    print("kamu benar!")
else:
    print("kamu salah! jawabannya adalah : " + random_choice)

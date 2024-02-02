import os

os.system("cls")
clue = """\n\n\n\nCLUE --> Kalo lu berguna, lu bakal dibutuhin 
         selalu oleh banyak orang 
         dan dideketin banyak orang. \n
    \t "Kalo tidak, lu hanya sampah (ga guna)." \n"""


def out(output):
    global clue
    clue = output


print(clue)
out(
    """Example : Gua butuh lo buat ini bro...\n
Example : Sinilah, bareng gua aja\n
Example : gimana? seru kan hehe...\n"""
)
print(clue)

print("Lihat fungsi (Tidak_Bermanfaat) \n")


def Tidak_Bermanfaat():
    a1 = """Lu ga gua butuhin bro!
        Tidak ada manfaatnya juga lu disini."""


Tidak_Bermanfaat()


def message(
    pesan="""Selagi lu bermanfaat bagi orang
           orang bakal, orang bakal sendirinya
           datang ke diri lo sendiri.\n\n\n\n""",
):
    return pesan


print("PESAN --> ", message())

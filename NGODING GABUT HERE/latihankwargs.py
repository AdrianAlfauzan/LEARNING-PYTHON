def inikwargs(*args, **data):
    nama = data["nama"]
    print("args : ", args)
    print(nama)


inikwargs(1, 2, 3, 4, 5, nama="adrian")

# Belajar tipe data dictionary

costumer = {"Name":"Eko", "Age":30, "Address":"Subang"}

name = costumer["Name"]
age = costumer["Age"]
addres = costumer["Address"]

costumer["Company"] = "X"
costumer["Name"] = "Eko Kurniawa"

del costumer["Address"]

for key, value in costumer.items():
    print(f"{key}:{value}")

import json

nom = input("Yangi mahsulot nomi: ")
yangi_miqdor = int(input("Yangi miqdor: "))

with open("products.json", "r") as f:
    data = json.load(f)

topildi = False
for item in data:
    if item["nom"] == nom:
        item["miqdor"] = yangi_miqdor
        topildi = True

if topildi:
    with open("products.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Miqdor yangilandi.")
else:
    print("Mahsulot topilmadi.")

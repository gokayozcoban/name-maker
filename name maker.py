import random

def isimOlusturucu():
    isim = ["Murat", "Orhan", "Nazlı", "Veli", "İbrahim", "Elif", "Zehra"]
    soyisim = ["Karlı", "Yaz", "Cengiz", "Yerli", "Kaya", "Yıldız", "Yurttaş"]
    return "{} {}".format(random.choice(isim), random.choice(soyisim))

for i in range(5):
    print(isimOlusturucu())

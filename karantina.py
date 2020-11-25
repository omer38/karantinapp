"""
türkiye sokağa çıkma yasağı saatlerini görmek için

"""
def hafta_içi_dışı(gün):
    if gün == "pazartesi" or gün == "salı" or gün == "çarşamba" or gün == "perşembe" or gün == "cuma":
        return "hafta içi"

    elif (gün == "cumartesi") or (gün == "pazar"):
        return "hafta sonu"

yas = int(input("merhabalar yasiniz kac? "))
gun = input("Hangi gundesiniz? ")
saat = float(input("Peki saat kac? "))

hafta_içi_dışı(gun)

if yas<20:
    if saat<=16 and saat>=13:
        print("sokağa çıkabilirsin dostum")
    else:
        print("dışarı çıkman yasak genç dostum")

elif yas>=20 and yas<65:

    if hafta_içi_dışı(gun) == "hafta içi":
        if (saat <= 20 and saat >= 10):
            print("Dışarı çıkabilirsiniz.")
        else:
            print("Dışarı çıkamazsınız.")
    elif hafta_içi_dışı(gun) == "hafta sonu":
        if (saat<=24 and saat>=20):
            print("dışarı çıkamazsınız")
        else:
            print("dışarı çıkabilirsiniz")


else:
    print("moruk sen zaten evde otur virüsü kaldıramazsın")



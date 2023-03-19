from cryptography.fernet import Fernet
import time
print("ByData Starting.....")
time.sleep(2)
print("..........ByData..........")
time.sleep(2)
print("ByData initialized successfully...")
time.sleep(2)
giris=input("ByData Veri Tabanina Girmek İçin Adinizi Giriniz...:")
time.sleep(2)
print("....................")
time.sleep(2)
print("Hoşgeldiniz Sayin",giris)

def dataİslemi():
    print("Bir txt oluşturmak için txt yi açmak istediğin yolu ve ardindan ismini yaz.")
    yeniDataOlustur=input("Data olusturmak istediğin dosyanin yolunu ve ismini yaz...:")
    dataVeriYazdirma= open(yeniDataOlustur,"w")
    yazdirma=input("verini düzenlemek istiyorsan bu kutucuğa yazarak düzenleyebilirsiniz...:")
    dataVeriYazdirma.write(yazdirma)
    time.sleep(2)
    print("Dataniniz başarili bir şekilde oluşruldu.")
    print("ByData'da yeni veri oluşturmak istemiyorsan sağ üst köşede bulunan 'x' tuşuna basarak çikabilirsin")

    sifre= Fernet.generate_key()


    with open("sifredosyasi.key", "wb") as sifredosyasi:
        sifredosyasi.write(sifre)

        f= Fernet(sifre)

    with open( yeniDataOlustur, "rb") as originalFile:
        original= originalFile.read()

        encrypted = f.encrypt(original)

    with open ("şifreli_"+yeniDataOlustur, "wb") as sifrelenmisDosya:
        sifrelenmisDosya.write(sifre)


while True:
    dataİslemi()
    time.sleep(2)

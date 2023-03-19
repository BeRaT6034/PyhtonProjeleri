import time

print("ByLogin Şifre Oluşturma Hizmetleri Başlatiliyor...")
time.sleep(2)
print("............ByLogin............")
time.sleep(2)
print("Merhaba. Şifrenizi oluşrurmak için gelecek olan metin kutusuna şifrenizi giriniz. Unutmayin! Gireceğiniz şifre sadece 4 karakter ile sinirlidir...")

def sifre():
    time.sleep(2)
    giris=input("Lütfen Oluştaracağiniz Şifreyi Girin...:")
    girisUzunluk=len(giris)
    if girisUzunluk <4 :
        print("Sifreniz 4 Karakter Boyutundan Küçük Olduğu İçin Kabul Görmemiştir...")
        time.sleep(2)
        print("Lütfen Tekrar Deneyin...")
        
    elif girisUzunluk >4:
        print("Sifreniz 4 Karakter Boyutunu Aştiği İçin Kabul Görmemiştir...")
        time.sleep(2)
        print("Lütfen Tekrar Deneyin...")

    if girisUzunluk == 4:
        print("Sifreniz Güncel Güvenlik Kurallarina Uyduğu İçin Şifreniz Kabul Görmüştür...")



while True:
    sifre()
    time.sleep(2)


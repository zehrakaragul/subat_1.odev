def hesap_makinesi(a, b):
    toplam = a + b
    fark = a - b
    carpim = a * b
    bolum = a / b if b != 0 else "Bölme hatası (b sıfır olamaz)"

    print(f"Toplam: {toplam}")
    print(f"Fark: {fark}")
    print(f"Çarpım: {carpim}")
    print(f"Bölüm: {bolum}")

def palindrom_mu(kelime):
    kelime = kelime.lower()
    if kelime == kelime[::-1]:
        return f"'{kelime}' palindromdur."
    else:
        return f"'{kelime}' palindrom değildir."

def yas_100_olma(yas):
    if yas >= 100:
        return "Zaten 100 yaşındasınız veya daha yaşlısınız!"
    else:
        kalan_yil = 100 - yas
        return f"{kalan_yil} yıl sonra 100 yaşına ulaşacaksınız."

# Ana program
while True:
    print("\n1. Hesap Makinesi")
    print("2. Palindrom Kontrolü")
    print("3. 100 Yaşına Ulaşma Hesaplama")
    print("4. Çıkış")
    
    secim = input("Bir seçenek girin: ")

    if secim == "1":
        a = float(input("Birinci sayıyı girin: "))
        b = float(input("İkinci sayıyı girin: "))
        hesap_makinesi(a, b)

    elif secim == "2":
        kelime = input("Bir kelime girin: ")
        print(palindrom_mu(kelime))

    elif secim == "3":
        yas = int(input("Yaşınızı girin: "))
        print(yas_100_olma(yas))

    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")

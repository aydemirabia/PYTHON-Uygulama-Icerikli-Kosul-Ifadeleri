# Bİr aracın yakıt tipine göre (benzin, dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu
# hesaplayan uygulama yazınız.

benzinFiyat = 19.01;
dizelFiyat = 23.71;
toplamYakitTuketimi = 0;

yakitTuketimi = float(input("100 KM // Ortalama Yakit Tuketimi: "));
gidilecekYol = float(input("Gidilecek Yol: "));
yakitTipi = str(input("Yakit Tipi: "));

toplamYakitTuketimi = gidilecekYol * (yakitTuketimi / 100);

if yakitTipi == "benzin":
    yakitMasrafi = toplamYakitTuketimi * benzinFiyat
    print(yakitMasrafi);
    
elif yakitTipi == "dizel":
    yakitMasrafi = toplamYakitTuketimi * dizelFiyat;
    print(yakitMasrafi);
else:
    print("Yanlis giris yaptiniz. Lutfen tekrar deneyiniz.");



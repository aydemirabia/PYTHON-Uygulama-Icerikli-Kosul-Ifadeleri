# Kişinin ad, kilo ve boy bilgilerini alınız.
#     Formül: (kilo / boy^2)
#         Vücut Kitle Kategorisi
#            0 - 18.4 -->Zayıf
#           18.5 - 24.9 --> Normal
#           25.0 - 29.9 --> Fazla Kilolu
#           30.0 - 34.9 --> Şişman(Obez)

isim=str(input("Adiniz: "));
soyisim=str(input("Soyad: "));
kilo=float(input("Kilo(KG): "));
boy=float(input("Boy(M): "));
vucutKitleIndeksi=float(kilo / (boy**2));

if vucutKitleIndeksi<=18.4:
    print(f'Sn {isim} {soyisim}; Vücut Kitle Indeksiniz: {vucutKitleIndeksi}\nZAYIF');
elif vucutKitleIndeksi>=18.5 and vucutKitleIndeksi<=24.9:
    print(f'Sn {isim} {soyisim}; Vücut Kitle Indeksiniz: {vucutKitleIndeksi}\nNORMAL');
elif vucutKitleIndeksi>=25.0 and vucutKitleIndeksi<=29.9:
    print(f'Sn {isim} {soyisim}; Vücut Kitle Indeksiniz: {vucutKitleIndeksi}\nFAZLA KILOLU');
elif vucutKitleIndeksi>=30.0 and vucutKitleIndeksi<=34.9:
    print(f'Sn {isim} {soyisim}; Vücut Kitle Indeksiniz: {vucutKitleIndeksi}\nSİSMAN (OBEZ)');
else:
    print("Lutfen gecerli degerler giriniz.");
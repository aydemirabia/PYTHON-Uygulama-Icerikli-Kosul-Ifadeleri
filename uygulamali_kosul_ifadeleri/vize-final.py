# Kullanicidan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırınız.
#       a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#       b) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1=int(input("VIZE 1: "));
vize2=int(input("VIZE 2: "));
final=int(input("FINAL: "));

ortalama=float(((vize1+vize2)/2)*0.6 +(final*0.4));

if final>=70:
    print(f'Final notunuz ortalamayi kapsamamaktadir. Tebrikler. GECTINIZ.');

elif ortalama>=50 and final>=50:
    print(f'Not ortalamaniz: {ortalama}\nGECTINIZ.');

else:
    print(f'Not ortalamaniz: {ortalama}\nKALDINIZ.')

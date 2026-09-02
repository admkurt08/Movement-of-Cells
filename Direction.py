import math

print("="*50)
print("HÜCRELER ARASI ETKİLEŞİMİ HESAPLAMA PROGRAMI")
print("="*50)
print()
print()
print("Ana Hücre Oluşturuldu. Güncel Konum 0/0/0")
changesincoordinate = int(input("Güncel Konumu Değiştirmek İster Misiniz Evet(1)/Hayır(2):   "))
print()
if changesincoordinate == 1:
    Xcordinateofsupercell = int(input("Lütfen X koordinatını giriniz:   "))
    Ycordinateofsupercell = int(input("Lütfen Y koordinatını giriniz:   "))
    Zcordinateofsupercell = int(input("Lütfen Z koordinatını giriniz:   "))
elif changesincoordinate == 2:
    print("Ulaşılmak İstenen Noktanın Koordinatlarını Yazınız:  ")
    print()
    Xcordinateofpoint = int(input("Lütfen X koordinatını giriniz:   "))
    Ycordinateofpoint = int(input("Lütfen Y koordinatını giriniz:   "))
    Zcordinateofpoint = int(input("Lütfen Z koordinatını giriniz:   "))
    Distance = math.sqrt((abs(Xcordinateofpoint))**2 + (abs(Ycordinateofpoint))**2 + (abs(Zcordinateofpoint))**2)

    print()
    print()
    print("="*50)
    print("MESAFE ve YÖN")
    print("="*50)


    
    



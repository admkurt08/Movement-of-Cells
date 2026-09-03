import math

print("=" * 60)
print("HÜCRELER ARASI ETKİLEŞİMİ HESAPLAMA PROGRAMI")
print("=" * 60)
print()

SuperCellX = 0.0
SuperCellY = 0.0
SuperCellZ = 0.0

print(f"Ana Hücre Oluşturuldu. Güncel Konum: {SuperCellX}/{SuperCellY}/{SuperCellZ}")
print()

changesincoordinate = int(input("Güncel Konumu Değiştirmek İster Misiniz Evet(1)/Hayır(2):   "))
print()

if changesincoordinate == 1:
     print("Yeni Ana Hücre Konumunu Giriniz")
     print()
     SuperCellX = float(input("Lütfen X koordinatını giriniz:   "))
     SuperCellY = float(input("Lütfen Y koordinatını giriniz:   "))
     SuperCellZ = float(input("Lütfen Z koordinatını giriniz:   "))
     print()
     print(f"Ana Hücre Yeni Konum: {SuperCellX}/{SuperCellY}/{SuperCellZ}")
     print()
elif changesincoordinate != 2:
     print("Geçersiz seçim.")
     raise SystemExit

print("Ulaşılmak İstenen Noktanın Koordinatlarını Yazınız")
print()
TargetX = float(input("Lütfen X koordinatını giriniz:   "))
TargetY = float(input("Lütfen Y koordinatını giriniz:   "))
TargetZ = float(input("Lütfen Z koordinatını giriniz:   "))

DX = TargetX - SuperCellX
DY = TargetY - SuperCellY
DZ = TargetZ - SuperCellZ

Distance = math.sqrt(DX**2 + DY**2 + DZ**2)
HorizontalAngle = math.degrees(math.atan2(DZ, DX))
HorizontalDistance = math.sqrt(DX**2 + DZ**2)
VerticalAngle = math.degrees(math.atan2(DY, HorizontalDistance))

print()
print("=" * 60)
print()

if HorizontalAngle > 0:
     print(f"Sağa Doğru {abs(HorizontalAngle):.2f} Derece Dönülecek")
elif HorizontalAngle < 0:
     print(f"Sola Doğru {abs(HorizontalAngle):.2f} Derece Dönülecek")
else:
     print("Sağ/Sol Dönüş Gerekmiyor")

if VerticalAngle > 0:
     print(f"Yukarı Doğru {abs(VerticalAngle):.2f} Derece Dönülecek")
elif VerticalAngle < 0:
     print(f"Aşağı Doğru {abs(VerticalAngle):.2f} Derece Dönülecek")
else:
     print("Yukarı/Aşağı Dönüş Gerekmiyor")

print()
print(f"Hedefe Olan Mesafe: {Distance:.4f}")
print()
print("=" * 60)
print("HESAPLAMA TAMAMLANDI")
print("=" * 60)

nilai = 60

if nilai > 70:
    print("Lulus")

nilai = 55

if nilai >= 60:
    print("Lulus")
else:
    print("Tidak Lulus")


nilai = 85

if nilai >= 85:
    print("A")
elif nilai >= 75:
    print("B")
elif nilai >= 60:
    print("C")
else:
    print("D")

try:
    angka = int(input("Masukkan angka: "))
    print("Angka:", angka)
except:
    print("Input harus berupa angka!")
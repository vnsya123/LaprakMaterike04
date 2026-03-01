try:
    bilangan = int(input("Masukkan bilangan: "))
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    else:
        print("Nol")
except:
    print("Input harus berupa angka!")


bilangan = int(input("Masukkan bilangan: "))
hasil = "Positif" if bilangan > 0 else "Negatif/Nol"
print(hasil)
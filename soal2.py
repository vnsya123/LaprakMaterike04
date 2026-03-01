try:
    bulan = int(input("Masukkan bulan (1-12): "))

    if bulan in [1,3,5,7,8,10,12]:
        print("Jumlah hari: 31")
    elif bulan in [4,6,9,11]:
        print("Jumlah hari: 30")
    elif bulan == 2:
        print("Jumlah hari: 29")
    else:
        print("Bulan tidak valid")
except:
    print("Input harus angka")
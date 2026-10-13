#Melakukan perulangan angka dari 1 hingga 50 (batas akhir 51 tidak dihitung)
for number in range (1, 51): 
    if number % 2 == 0 and number % 5 == 0:  #Mengecek apakah angka habis dibagi 2 DAN habis dibagi 5 secara bersamaan (kelipatan 10)
        print("HelloWorld")
    elif number % 2 == 0: #Jika kondisi pertama tidak terpenuhi, cek apakah angka hanya habis dibagi 2 (angka genap)
        print("Hello")
    elif number % 5 == 0: #Jika kondisi sebelumnya tidak terpenuhi, cek apakah angka hanya habis dibagi 5
        print("World")
    else:  #Jika semua kondisi di atas tidak terpenuhi (angkanya bukan kelipatan 2 ataupun 5)
        print(number) #Cetak angka aslinyad
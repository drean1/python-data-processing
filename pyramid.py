#Menentukan jumlah baris (tinggi) dari pola yang akan dibuat, yaitu 5 baris
n = 5
for i in range(n):  #Loop luar (outer loop) untuk mengatur perpindahan tiap baris (berjalan dari 0 hingga 4)
    #Loop dalam (inner loop) untuk mencetak jumlah bintang pada baris tersebut
    #Jumlah bintang bertambah 1 di setiap barisnya mengikuti nilai 'i'
    for j in range(i + 1): 
        print("*", end="") #Mencetak karakter bintang ("*") tanpa otomatis pindah ke baris baru (tetap ke samping)
    print() #Mencetak baris baru (enter) agar pencetakan bintang selanjutnya dimulai dari bawahaa
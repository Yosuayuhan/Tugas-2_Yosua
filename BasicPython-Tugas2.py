menu = 1
nama = []
telepon = []


print(" \n \n Selamat Datang!")

def tambahkontak():

        print(" \n \n ")
        inputnama = input("Nama : ")
        inputtelepon = input("No Telepon : ")
        nama.append(inputnama)
        telepon.append(inputtelepon)
        

while menu != 3:
    print(" \n \n ====Menu====== \n1 Daftar Kontak \n2 Tambah Kontak \n3 Keluar")

    

    menu = int(input("Pilih menu : "))
    
    if menu == 1:
        print(" \n \n Daftar Kontak")

        jumlahkontak = len(nama)

        urutan = 0
        
        
        while urutan < jumlahkontak:
            
            print("Nama :", nama[urutan])
            print("No Telepon :", telepon[urutan])
            urutan = urutan + 1

    if menu == 2:
        tambahkontak()

    if menu > 3:
        print(" \n \n Menu tidak tersedia")

    if menu == 3:
        break

print(" \n \n Program selesai, sampai jumpa!")



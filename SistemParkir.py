#membuat fungsi biaya parkir dengan parameter kendaraan dan durasi

def biaya_parkir(kendaraan, durasi):
    if kendaraan == "mobil": 
        tarif_kendaraan = 5000
        print("Tarif parkir mobil Rp5000")
        #jika user menginput kendaraan adalah mobil maka akan mengeprint "Tarif parkir mobil Rp5000"
    elif kendaraan == "motor":
        tarif_kendaraan = 3000
        print("Tarif parkir motor Rp3000")
        #jika user menginput kendaraan adalah motor maka akan mengeprint "Tarif parkir motor Rp3000"
    else:
        return None
    
    return tarif_kendaraan * durasi
    #menghitung biaya parkir dengan mengalikan tarif_kendaraan dan durasi

kendaraan = input("Masukkan jenis kendaraan anda: ")
jam_masuk = int(input("Masukkan jam masuk: "))
jam_keluar = int(input("Masukkan jam keluar: "))

durasi = jam_keluar - jam_masuk
#untuk mengetahui durasi parkir kendaraan, kita akan mengurangi jam kendaraan keluar dan jam kendaraan masuk

total_biaya_parkir = biaya_parkir(kendaraan, durasi)
#digunakan untuk menjalankan fungsi biaya_parkir

print("== Struk Total Biaya Parkir ==")
print("Jenis kendaraan: ", kendaraan)
print("Jam masuk: ", jam_masuk)
print("Jam keluar: ", jam_keluar)
print("Durasi parkir: ", durasi)
print("Total biaya parkir: ", total_biaya_parkir)

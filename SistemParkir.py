def biaya_parkir(kendaraan, durasi):
    if kendaraan == "mobil":
        tarif_kendaraan = 5000
        print("Tarif parkir mobil Rp5000")
    elif kendaraan == "motor":
        tarif_kendaraan = 3000
        print("Tarif parkir motor Rp3000")
    else:
        return None
    
    return tarif_kendaraan * durasi

kendaraan = input("Masukkan jenis kendaraan anda: ")
jam_masuk = int(input("Masukkan jam masuk: "))
jam_keluar = int(input("Masukkan jam keluar: "))

durasi = jam_keluar - jam_masuk

total_biaya_parkir = biaya_parkir(kendaraan, durasi)

print("== Struk Total Biaya Parkir ==")
print("Jenis kendaraan: ", kendaraan)
print("Jam masuk: ", jam_masuk)
print("Jam keluar: ", jam_keluar)
print("Durasi parkir: ", durasi)
print("Total biaya parkir: ", total_biaya_parkir)
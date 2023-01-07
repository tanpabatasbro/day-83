#memprediksi keuntungan investasi

modal = int(input("Masukkan Jumlah Moda Awal Investasi : "))
lama = int(input("Masukkan Berapa Tahun Investasi : "))
untung = 5/100

keuntungan = ((modal * untung) * lama)
hasil = keuntungan + modal
print(f"keuntungan investasi sebanyak 5% setelah {lama} Tahun adalah :{keuntungan}")
print(f"Total Modal Awal ditambah Keuntungan : {hasil}")


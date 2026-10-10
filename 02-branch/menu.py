# Daftar menu warung sederhana untuk latihan branch.
# Di latihan, kamu akan menambah minuman di branch terpisah.

menu = ["Nasi Goreng", "Mie Ayam"]

for nomor, makanan in enumerate(menu, start=1):
    print(f"{nomor}. {makanan}")

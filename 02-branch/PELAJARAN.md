# Pelajaran 02: Branch

## 1. Apa itu Branch?

Branch (cabang) adalah **jalur kerja terpisah** di dalam satu repo.

Bayangkan kamu punya buku resep. Kamu ingin mencoba resep baru, tapi tidak
mau mencoret-coret buku aslinya. Jadi kamu **fotokopi** bukunya, mencoba di
fotokopian itu, dan kalau berhasil baru disalin ke buku asli.

- Buku asli = branch utama (biasanya bernama **`main`**)
- Fotokopian = branch baru (misalnya **`tambah-minuman`**)

```
main            ●──────●───────────────●   <- versi "resmi" yang selalu aman
                        \             /
tambah-minuman           ●─────●─────     <- tempat mencoba hal baru
                       (coba) (coba)   (merge = gabungkan kembali)
```

## 2. Kenapa Branch Penting?

1. **Aman.** Kalau percobaan gagal, branch `main` tidak ikut rusak.
2. **Bisa kerja bareng.** Dhani mengerjakan fitur A di satu branch, teman
   mengerjakan fitur B di branch lain, dan tidak saling ganggu.
3. **Bisa direview.** Sebelum digabung ke `main`, perubahan bisa dicek dulu
   lewat **Pull Request** (Pelajaran 03).

## 3. Perintah Dasar Branch

| Perintah | Fungsinya |
|----------|-----------|
| `git branch` | Lihat daftar branch (tanda `*` = branch yang sedang aktif) |
| `git switch -c nama-branch` | **Buat** branch baru dan langsung pindah ke sana |
| `git switch nama-branch` | **Pindah** ke branch yang sudah ada |
| `git merge nama-branch` | **Gabungkan** branch lain ke branch yang sedang aktif |
| `git branch -d nama-branch` | **Hapus** branch yang sudah selesai digabung |

> Di tutorial lama kamu mungkin melihat `git checkout -b`. Fungsinya sama
> dengan `git switch -c`, hanya `switch` lebih baru dan lebih mudah diingat.

## 4. Contoh Nyata (hasil asli dari terminal)

File [`menu.py`](menu.py) awalnya berisi 2 makanan. Kita tambah minuman
**di branch terpisah**:

```console
$ git branch
* main

$ git switch -c tambah-minuman
Switched to a new branch 'tambah-minuman'

# ... edit menu.py, tambahkan "Es Teh", lalu commit ...
$ git commit -am "Tambah Es Teh ke menu"

$ python3 menu.py            # di branch tambah-minuman
1. Nasi Goreng
2. Mie Ayam
3. Es Teh

$ git switch main
Switched to branch 'main'

$ python3 menu.py            # di branch main -> Es Teh BELUM ada!
1. Nasi Goreng
2. Mie Ayam
```

👆 Inilah inti branch: **file yang sama bisa punya isi berbeda di branch
berbeda.** Begitu pindah branch, Git otomatis mengganti isi file.

Kalau sudah yakin, gabungkan ke `main`:

```console
$ git merge tambah-minuman
Updating ef5d354..f82837f
Fast-forward
 menu.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

$ python3 menu.py            # sekarang main juga punya Es Teh
1. Nasi Goreng
2. Mie Ayam
3. Es Teh

$ git branch -d tambah-minuman
Deleted branch tambah-minuman (was f82837f).
```

(Kode seperti `ef5d354` adalah ID commit. Di komputermu angkanya akan berbeda.)

💡 **Fast-forward** artinya `main` tidak berubah sejak branch dibuat, jadi Git
cukup "memajukan" `main` ke commit terbaru. Tidak ada yang perlu dicampur.

## 5. Tips Memberi Nama Branch

- Pakai huruf kecil dan tanda hubung: `tambah-minuman`, `perbaiki-typo-readme`
- Jelaskan **tujuannya**, bukan nama orang: ✅ `tambah-halaman-kontak`, ❌ `branch-dhani`
- Branch berawalan `claude/...` di repo ini adalah branch yang dibuat oleh Claude
  saat membantu kamu.

## ✏️ Latihan (langsung di website GitHub)

**Bagian A: Buat branch `main` dan jadikan branch utama**

Repo ini dibuat kosong, jadi branch pertama yang dikirim (`claude/...`)
otomatis menjadi branch utama. Mari rapikan:

1. Di halaman repo, klik tombol dropdown branch (kiri atas, ada ikon cabang 🔀).
2. Ketik `main`, lalu klik **Create branch main from claude/...**.
3. Buka **Settings → General → Default branch**, klik ikon ⇄, pilih `main`,
   lalu **Update** dan konfirmasi.

Sekarang halaman depan repo menampilkan branch `main`.

**Bagian B: Coba kerja di branch baru**

1. Dari dropdown branch, pastikan sedang di `main`, lalu buat branch baru
   bernama `tambah-minuman`.
2. Di branch `tambah-minuman`, buka `02-branch/menu.py`, klik ✏️, ubah baris
   menu menjadi:
   ```python
   menu = ["Nasi Goreng", "Mie Ayam", "Es Teh"]
   ```
3. Commit dengan pesan `Tambah Es Teh ke menu`.
4. Pindah ke branch `main` lewat dropdown, lalu buka `menu.py` lagi.
   **Es Teh belum ada di sana!** Itu artinya branch bekerja dengan benar.

GitHub mungkin menampilkan kotak kuning *"tambah-minuman had recent pushes"*
dengan tombol **Compare & pull request**. Jangan diklik dulu. Itu bahan
**Pelajaran 03: Pull Request**. 😉

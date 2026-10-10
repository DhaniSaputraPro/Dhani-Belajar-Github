# Pelajaran 01: Repository, Commit & README

## 1. Apa itu Git dan GitHub?

- **Git** = alat untuk mencatat *riwayat perubahan* file. Bayangkan seperti
  fitur "Save" di game: kamu bisa kembali ke save point mana pun.
- **GitHub** = website tempat menyimpan repo Git secara online, supaya bisa
  di-backup, dibagikan, dan dikerjakan bareng orang lain.

## 2. Apa itu Repository (Repo)?

Repository = **folder proyek** yang dipantau oleh Git.
Repo ini (`Dhani-Belajar-Github`) adalah contoh repository.

```
Dhani-Belajar-Github/          <- ini repository
├── README.md                  <- halaman depan repo
└── 01-repository-dan-commit/
    ├── PELAJARAN.md           <- file yang sedang kamu baca
    └── halo.py                <- contoh code
```

### Halaman "Create a new repository" (github.com/new)

Saat membuat repo ini, semua pilihan dibiarkan bawaan (default). Ini arti
setiap pilihannya:

| Pilihan | Artinya | Pilihan saat repo ini dibuat |
|---------|---------|------------------------------|
| **Owner / Repository name** | Pemilik dan nama repo. Jadi alamatnya `github.com/DhaniSaputraPro/<nama>` | `Dhani-Belajar-Github` |
| **Description** | Kalimat pendek yang tampil di halaman repo (boleh kosong) | kosong |
| **Visibility** | **Public** = semua orang bisa *melihat*. **Private** = hanya kamu dan orang yang kamu undang. (Yang bisa *mengubah* tetap hanya kamu dan kolaborator.) | Public |
| **Add README** | Langsung membuat file `README.md` beserta commit pertama | Off |
| **Add .gitignore** | Daftar file yang tidak perlu disimpan Git (dibahas di Pelajaran 06) | No .gitignore |
| **Add license** | Aturan boleh/tidaknya orang lain memakai code kamu (misalnya MIT) | No license |

Karena **Add README = Off**, repo ini awalnya **benar-benar kosong**: tidak ada
file dan tidak ada commit. Commit pertama baru dibuat bersama pelajaran ini.
Kalau README dinyalakan, GitHub langsung membuat commit pertama bernama
*"Initial commit"* yang berisi `README.md`.

💡 Semua pilihan ini bisa ditambahkan nanti. README, `.gitignore`, dan license
hanyalah file biasa, dan Visibility bisa diubah di **Settings** repo.

## 3. Apa itu Commit?

Commit = **satu "save point"** yang berisi:
- perubahan apa saja yang dibuat,
- siapa yang membuat,
- kapan,
- dan **pesan** yang menjelaskan perubahannya.

Perumpamaan: seperti **mengirim paket** 📦

| Langkah | Perintah | Perumpamaan |
|---|---|---|
| 1 | *(edit file)* | Menyiapkan barang |
| 2 | `git add` | Memasukkan barang ke kardus |
| 3 | `git commit -m "..."` | Menutup kardus dan menempel label isinya |
| 4 | `git push` | Menyerahkan kardus ke kurir, lalu dikirim ke GitHub |

> 🌐 **Kalau pakai website GitHub:** cukup edit file (ikon ✏️), isi pesan, lalu
> klik tombol hijau **Commit changes**. Langkah 2, 3, dan 4 terjadi sekaligus.
> Perintah di bawah ini hanya diperlukan kalau kamu bekerja di terminal
> komputer sendiri.

Alur kerja dasar di terminal ada 4 langkah (baris berawalan `#` hanya catatan,
tidak ikut dijalankan):

```bash
# 1. Ubah / buat file (misalnya edit halo.py)

# 2. "Masukkan ke keranjang" (staging) file yang mau di-commit
git add halo.py

# 3. Simpan save point dengan pesan yang jelas
git commit -m "Tambah program halo dunia"

# 4. Kirim ke GitHub (online)
git push
```

Lihat riwayat commit:

```bash
git log --oneline
```

💡 **Tips pesan commit yang baik:** singkat, jelas, dan menjelaskan *apa* yang
berubah. Contoh bagus: `Tambah fungsi sapa`. Contoh kurang bagus: `update`.

## 4. Apa itu README.md?

`README.md` adalah file yang **otomatis ditampilkan** di halaman depan repo
GitHub. Formatnya **Markdown** (`.md`), cara menulis teks berformat yang simpel:

| Kamu tulis          | Hasilnya              |
|---------------------|-----------------------|
| `# Judul`           | Judul besar           |
| `## Sub judul`      | Judul lebih kecil     |
| `**tebal**`         | **tebal**             |
| `*miring*`          | *miring*              |
| `- item`            | daftar berpoin        |
| `[teks](link)`      | [tautan](https://github.com) |
| `` `code` ``        | `code`                |

## 5. Contoh Code

Lihat file [`halo.py`](halo.py). Jalankan dengan:

```bash
python3 01-repository-dan-commit/halo.py
```

## ✏️ Latihan

1. Buka file `halo.py` langsung di website GitHub, klik ikon pensil ✏️ (Edit).
2. Ganti nama `"Dhani"` dengan nama teman kamu.
3. Di bawah, isi pesan commit, misalnya `Ganti nama di halo.py`, lalu klik
   **Commit changes**.
4. Klik tab **Commits** (ikon jam 🕒 di halaman repo) — kamu akan lihat
   commit kamu muncul di riwayat. Klik commit itu untuk melihat baris mana yang
   berubah (merah = dihapus, hijau = ditambah).

Selamat, kamu sudah membuat commit pertama! 🎉

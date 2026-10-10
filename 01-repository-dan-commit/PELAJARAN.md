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

## 3. Apa itu Commit?

Commit = **satu "save point"** yang berisi:
- perubahan apa saja yang dibuat,
- siapa yang membuat,
- kapan,
- dan **pesan** yang menjelaskan perubahannya.

Alur kerja dasar ada 3 langkah:

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

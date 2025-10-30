# 🃏 GREXCARD

**GREXCARD** adalah proyek permainan kartu berbasis *poker-like logic* yang dikembangkan sepenuhnya menggunakan pendekatan **AI-assisted coding vibe**.  
Game ini dimulai sebagai *text-based CLI prototype*, dan akan berkembang menjadi game kartu strategi dengan sistem kombinasi, efek kartu, serta mekanik unik di masa depan.

---

## 🎮 Versi Saat Ini: `v0.2` — Playable Foundation

Versi ini menandai **rangka awal permainan** GREXCARD:
- Pemain sudah bisa **memulai permainan dari CLI**
- **Deck system** sudah berfungsi penuh (shuffle & draw)
- **Main menu** tersedia untuk interaksi pemain
- Struktur kode sudah modular di dalam folder `src/`

---

## 🧱 Struktur Proyek
grexcard/
│
├── src/
│ └── grexcard.py # Script utama game
│
├── docs/
│ └── DEV_GUIDE.md # Panduan pengembang
│
├── README.md
└── requirements.txt

yaml
Copy code

---

## 🧩 Rencana Versi Selanjutnya (`v0.3`)
- Implementasi **evaluasi tangan poker**
- Penambahan sistem **scoring dan ronde**
- Lawan komputer (*AI opponent basic*)
- Efek visual teks (*animated CLI*)

---

## 💡 Filosofi Pengembangan
> GREXCARD bukan hanya proyek game, tapi juga eksperimen eksploratif tentang bagaimana **AI dan manusia dapat berkolaborasi membangun game dari nol**.  
> Tujuan utamanya adalah menciptakan ekosistem *coding vibe* yang ringan, kreatif, dan dapat berkembang bersama komunitas.

---

## ⚙️ Menjalankan Proyek
1. Pastikan sudah menginstal Python 3.10+
2. Clone repositori:
   ```bash
   git clone https://github.com/HyugaKjr/grexcard.git
   cd grexcard
Jalankan game:

bash
Copy code
python src/grexcard.py
🪪 Lisensi
Proyek ini dilisensikan di bawah MIT License.

👥 Kontribusi
Kami sangat terbuka terhadap kontribusi dari siapa pun!
Jika kamu punya ide, bug fix, atau tambahan fitur — silakan buat issue atau pull request.

© 2025 GREXCARD Project — Made with 💻 + 🤖 (AI-assisted coding)

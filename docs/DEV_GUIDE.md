
### Modul Utama
- **grexcard.py**  
  Menjalankan game utama, menangani input pengguna, dan mengontrol alur permainan.
- **deck system (akan datang di v0.2)**  
  Mengelola kartu, efek, dan kombinasi.
- **player system (akan datang di v0.2)**  
  Menyimpan status pemain (koin, skor, kartu aktif, dll).

---

## 🎮 Alur Game (Versi 0.1)

1. **Startup**  
   Program menampilkan menu utama berbasis teks.
2. **Draw Cards**  
   Pemain menarik sejumlah kartu dari deck.
3. **Play Phase**  
   Pemain memilih kartu untuk dimainkan.
4. **Result Phase**  
   Hasil kombinasi dihitung, skor diperbarui.
5. **End / Retry**  
   Pemain dapat mencoba lagi atau keluar dari game.

---

## 🧠 Desain Sistem Kartu

Setiap kartu direpresentasikan dalam bentuk **objek sederhana (dictionary)** seperti berikut:

```python
{
    "name": "Ace of Spades",
    "value": 14,
    "suit": "Spades",
    "effect": None
}

import random

# ====== Inisialisasi deck kartu ======
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def buat_deck():
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# ====== Evaluasi kombinasi sederhana ======
def evaluasi_kombinasi(kartu_terpilih):
    ranks_kartu = [k[:-1] for k in kartu_terpilih]
    suits_kartu = [k[-1] for k in kartu_terpilih]

    rank_count = {r: ranks_kartu.count(r) for r in ranks_kartu}

    if len(set(suits_kartu)) == 1:
        return "Flush", 150
    elif 3 in rank_count.values():
        return "Three of a Kind", 120
    elif list(rank_count.values()).count(2) == 1:
        return "Pair", 80
    else:
        return "High Card", 40

# ====== Fungsi utama permainan ======
def main():
    skor_total = 0
    ronde = 1
    max_ronde = 5

    print("====================================")
    print("🃏 GREXCARD - Versi CLI 🎴")
    print("====================================")

    while ronde <= max_ronde:
        print(f"\nRonde {ronde}")
        deck = buat_deck()
        hand = deck[:5]

        # Tampilkan kartu
        print("Kartu kamu:")
        for i, kartu in enumerate(hand, start=1):
            print(f"[{i}] {kartu}", end="  ")
        print("\n")

        # Input pilihan kartu
        while True:
            try:
                pilihan = input("Pilih 3 kartu (misal: 1,3,5): ").replace(" ", "")
                idx = [int(x) - 1 for x in pilihan.split(",") if x.isdigit()]
                if len(idx) == 3 and all(0 <= i < len(hand) for i in idx):
                    break
                else:
                    print("Input tidak valid! Pilih 3 nomor kartu yang tersedia.")
            except ValueError:
                print("Masukan tidak valid. Coba lagi.")

        kartu_terpilih = [hand[i] for i in idx]
        kombinasi, skor = evaluasi_kombinasi(kartu_terpilih)

        print(f"\nKombinasi: {kombinasi}")
        print(f"Skor didapat: +{skor}")
        skor_total += skor
        print(f"Skor total: {skor_total}")
        print("------------------------------------")

        if ronde < max_ronde:
            input("Tekan Enter untuk lanjut ke ronde berikutnya...")
        ronde += 1

    print("\n====================================")
    print("🎯 Permainan Selesai!")
    print(f"Total Skor Akhir: {skor_total}")
    print("Terima kasih sudah bermain GREXCARD!")
    print("====================================")

# ====== Jalankan game ======
if __name__ == "__main__":
    main()

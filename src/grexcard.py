import random
import os
import sys

# ==========================================
# GREXCARD v0.2 - Playable Foundation (CLI)
# ==========================================

# Representasi 1 kartu (rank + suit)
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Kumpulan kartu (deck)
class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

# Pemain
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        card = deck.draw()
        if card:
            self.hand.append(card)

    def show_hand(self):
        return ", ".join(str(card) for card in self.hand)

# Permainan utama
class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = None

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self):
        while True:
            self.clear()
            print("=== GREXCARD v0.2 ===")
            print("1. Main Classic Draw")
            print("2. Tentang Game")
            print("3. Keluar")

            choice = input("Pilih menu (1-3): ").strip()
            if choice == "1":
                self.play_classic_draw()
            elif choice == "2":
                self.about()
            elif choice == "3":
                print("\nTerima kasih telah mencoba GREXCARD!")
                sys.exit()
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk kembali...")

    def about(self):
        self.clear()
        print("=== Tentang GREXCARD ===")
        print("Versi: 0.2 (Playable Foundation)\n")
        print("GREXCARD adalah game kartu text-based yang terinspirasi dari poker,")
        print("namun dikembangkan dengan bantuan AI (coding vibe) secara iteratif.")
        print("\nTujuan proyek ini adalah membangun game modular,")
        print("dimulai dari versi CLI sederhana hingga menjadi game penuh.")
        input("\nTekan Enter untuk kembali ke menu utama...")

    def play_classic_draw(self):
        self.clear()
        name = input("Masukkan nama pemain: ").strip()
        self.player = Player(name)
        self.deck = Deck()  # reset deck baru setiap permainan
        self.deck.shuffle()

        print(f"\nHalo {self.player.name}, selamat datang di mode Classic Draw!")
        print("Kamu akan menarik 5 kartu dari deck.\n")

        for _ in range(5):
            self.player.draw_card(self.deck)

        print("Kartu kamu:")
        print(self.player.show_hand())

        input("\nTekan Enter untuk kembali ke menu utama...")

if __name__ == "__main__":
    game = Game()
    game.start()

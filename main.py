"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Daniel Polášek
email: sidzej111@seznam.cz
"""


import random

# Funkce generování tajného čísla
def generovani_tajneho_cisla():
    return ''.join(random.sample('1234567890', 4))

# Kontrolní funkce, zda je tip validní
def validni_tip(guess):
    return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4

# Funkce vyhodnocování tipu
def vyhodnoceni_tipu(secret, guess):
    bulls = sum(1 for i in range(4) if secret[i] == guess[i])
    cows = sum(1 for i in range(4) if guess[i] in secret and secret[i] != guess[i])
    return bulls, cows

# Funkce zobrazení správného formátu
def zobrazeni_spravneho_formatu(bulls, cows):
    print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
    print("-" * 47)

# Hlavní funkce programu
def main():
    print("Hi there!\n" + "-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.\n" + "-" * 47)
    
    secret_number = generovani_tajneho_cisla()
    attempts = 0

    while True:
        
        if attempts == 0:
            guess = input('Enter a number (or type "exit" to quit the game):\n>>> ')
        else:
            guess = input('>>> ')

        if guess.lower() == "exit":
            print("Exiting the game. Goodbye!")
            break
        
        if not validni_tip(guess):
            print("Invalid guess! Try again.")
            continue
        
        attempts += 1
        bulls, cows = vyhodnoceni_tipu(secret_number, guess)

        # Vyhodnocení správného tipu
        if bulls == 4:
            print(f"Correct, you've guessed the right number\nin {attempts} guesses!")
            print("-" * 47)
            print("That's amazing!")
            break

        zobrazeni_spravneho_formatu(bulls, cows)

if __name__ == "__main__":
    main()

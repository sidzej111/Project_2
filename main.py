"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Daniel Polášek
email: sidzej111@seznam.cz
"""


import random

# Funkce generování tajného čísla
def generovani_tajneho_cisla():
    cisla = random.sample('0123456789', 4)
    return ''.join(cisla)

# Kontrolní funkce, zda je tip validní
def validni_tip(guess):
    if len(guess) != 4:
        return False, "The guess must be exactly 4 digits.\n" + "-" * 47
    if not guess.isdigit():
        return False, "The guess must contain only digits.\n" + "-" * 47
    if guess[0] == '0':
        return False, "The guess cannot start with a zero.\n" + "-" * 47
    if len(set(guess)) != 4:
        return False, "All digits in the guess must be unique.\n" + "-" * 47
    return True, ""

# Funkce vyhodnocování tipu
def vyhodnoceni_tipu(secret, guess):
    bulls = 0
    cows = 0

    tajne_cislo = [0] * 10
    tip = [0] * 10

    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            tajne_cislo[int(secret[i])] += 1
            tip[int(guess[i])] += 1

    for i in range(10):
        cows += min(tajne_cislo[i], tip[i])

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
            guess = input(f"Enter a number (or type \"exit\" to quit the game):\n>>> ")
        else:
            guess = input(f">>> ")

        if guess.lower() == "exit":
            print("Exiting the game. Goodbye!\n" + "-" * 47)
            break
        
        valid, error_message = validni_tip(guess)
        
        if not valid:
            print(error_message)
            continue
        
        attempts += 1
        bulls, cows = vyhodnoceni_tipu(secret_number, guess)

        if bulls == 4:
            print(f"Correct, you've guessed the right number\nin {attempts} guesses!")
            print("-" * 47)
            print("That's amazing!")
            break

        zobrazeni_spravneho_formatu(bulls, cows)

if __name__ == "__main__":
    main()

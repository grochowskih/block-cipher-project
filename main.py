from decrypt import decrypt
from encrypt import encrypt
import re

if __name__ == "__main__":
    run = "1"
    while run == "1":
        print("Wybierz opcję, którą chcesz wykonać:")
        print("1) Przykładowe dane, które pokazują, że algorytm działa")
        print("2) Zaszyfruj wiadomość")
        print("3) Deszyfruj wiadomość")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            print("Do sth")
        elif choice == "2":
            mes = input("Podaj wiadomość jako ciąg 64 bitów, którą chcesz zaszyfrować:" )
            key = input("Podaj klucz jako ciąg 64 bitów, którego chcesz użyć: ")
            if re.match("^[01]+$", mes) is None or re.match("^[01]+$", key) is None:
                print("Wiadomość/Klucz ma być ciągiem bitów!")
            else:
                enc = encrypt(mes, key)
                print("Wynik szyfrowania to: ")
                print(enc)
        elif choice == "3":
            mes = input("Podaj wiadomość jako ciąg 64 bitów, którą chcesz deszyfrować:" )
            key = input("Podaj klucz jako ciąg 64 bitów, którego chcesz użyć: ")
            if re.match("^[01]+$", mes) is None or re.match("^[01]+$", key) is None:
                print("Szyfrogram/Klucz ma być ciągiem bitów!")
            else:
                dec = decrypt(mes, key)
                print("Wynik deszyfrowania to: ")
                print(dec)
        else:
            print("Błędny wybór!")
        run = input("Czy chcesz kontynuować, jeśli tak, to wybierz 1: ")

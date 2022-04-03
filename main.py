from decrypt import decrypt
from encrypt import encrypt
import re
import time

from examples import examples

if __name__ == "__main__":
    run = "1"
    while run == "1":
        print("Wybierz opcję, którą chcesz wykonać:")
        print("1) Przykładowe dane, które pokazują, że algorytm działa")
        print("2) Zaszyfruj wiadomość")
        print("3) Deszyfruj wiadomość")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            start = time.time()
            try:
                for case in examples:
                    print("Szfyrowana wiadomosc: ", case[0])
                    print("Uzyty klucz: ", case[1])
                    enc = encrypt(case[0], case[1])
                    print("Wynik szyfrowania: ", enc)
                    dec = decrypt(enc, case[1])
                    print("Wynik deszyfrowania: ", dec)
                    print("Czy wiadomość jest równa złożeniu deszyfrowania i szyfrowania? ", dec == case[0])
            except Exception as ex:
                print(ex)
            end = time.time()
            print("Czas wykonania ", len(examples), " operacji szyfrowania i deszyfrowania wyniósł: ", end - start)
        elif choice == "2":
            mes = input("Podaj wiadomość jako ciąg 64 bitów, którą chcesz zaszyfrować: ")
            key = input("Podaj klucz jako ciąg 64 bitów, którego chcesz użyć: ")
            try:
                if re.match("^[01]+$", mes) is None or re.match("^[01]+$", key) is None:
                    print("Wiadomość/Klucz ma być ciągiem bitów!")
                else:
                    enc = encrypt(mes, key)
                    print("Wynik szyfrowania to: ")
                    print(enc)
            except Exception as ex:
                print(ex)
        elif choice == "3":
            mes = input("Podaj wiadomość jako ciąg 64 bitów, którą chcesz deszyfrować: ")
            key = input("Podaj klucz jako ciąg 64 bitów, którego chcesz użyć: ")
            try:
                if re.match("^[01]+$", mes) is None or re.match("^[01]+$", key) is None:
                    print("Szyfrogram/Klucz ma być ciągiem bitów!")
                else:
                    dec = decrypt(mes, key)
                    print("Wynik deszyfrowania to: ")
                    print(dec)
            except Exception as ex:
                print(ex)
        else:
            print("Błędny wybór!")
        run = input("Czy chcesz kontynuować, jeśli tak, to wybierz 1: ")

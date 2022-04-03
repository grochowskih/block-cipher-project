from generators import generate_key, s_box, shift_repeat_right



def encrypt(plaintext, key):
    """
    encrypt

    Input
    ----------
    plaintext, key
    len(plaintext)=len(key)=64

    Output
    -------
    ciphertext

    """
    if len(plaintext) != 64:
        raise Exception("Niepoprawny rozmiar zmiennej plaintext!") 
    if len(key) != 64:
        raise Exception("Niepoprawny rozmiar zmiennej key!")    
    #Sprawdzenie dlugosci danych wejsciowych

    L=plaintext[0:32]
    R=plaintext[32:64]
    #Podzial plaintextu na 2 bloki 32-bitowe

    for i in range(1,17):
        round_key=generate_key(key, i)
        R_temp=int(R,2)^int(round_key,2) #XOR z kluczem
        R_temp=shift_repeat_right(bin(R_temp)[2:],i).zfill(32) #Przesuniecie o i bitów w prawo
        R_temp=s_box(round_key, R_temp)
        L_temp=int(L,2)
        L=R #Prawy blok staje sie lewym
        R=bin(int(R_temp,2)^L_temp)[2:].zfill(32) #XOR lewego bloku z wyjsciem z funkcji f

    ciphertext=L+R #Polaczenie lewego i prawego bloku      
    return ciphertext
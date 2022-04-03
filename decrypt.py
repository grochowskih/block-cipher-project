from generators import generate_key, s_box, shift_repeat_right


def decrypt(ciphertext, key):
    """
    Funkcja realizująca deszyfrowanie w naszym zaprojektowanym szyfrze blokowym.
    :param ciphertext: Wiadomość do odszyfrowania (zapisana binarnie jako string długości 64 bitów)
    :param key: Klucz (zapisany binarnie jako string długości 64 bitów)
    :return: Wiadomość (binarnie jako string), po której zaszyfrowaniu otrzymaliśmy ciphertext
    """
    if len(ciphertext) != 64:
        raise Exception("Błędna długość szyfrogramu!")
    if len(key) != 64:
        raise Exception("Błędna długość klucza!")

    left = ciphertext[0:32]
    right = ciphertext[32:64]

    for i in range(0,32):
        round_key = generate_key(key, 31 - i)
        new_left = "{0:032b}".format(int(left, 2) ^ int(round_key, 2))
        new_left = shift_repeat_right(new_left, 31 - i)
        new_left = s_box(round_key, new_left)
        new_left = int(new_left, 2) ^ int(right, 2)

        old_left = left
        left = "{0:032b}".format(new_left)
        right = old_left

    return left + right


import sboxes

def generate_key(main_key, round):
    """
    Funkcja generująca klucz rundowy.
    :param main_key: Klucz główny (zapisany binarnie jako string długości 64 bitów)
    :param round: Numer rundy (od 1 do 16)
    :return: Klucz rundowy (zapisany binarnie jako string długości 64 bitów)
    """

    left = main_key[0:32]
    right = main_key[32:64]

    if round % 2 == 0:
        left = left << round
        right = right >> round
    else:
        left = left >> round
        right = right << round

    return left + right


def s_box(round_key, arg):
    """
    Funkcja, która wybiera w zależności od klucza rundowego odpowiednie SBoxy i wylicza wartość funkcji.
    :param round_key: Klucz rundowy (zapisany binarnie jako ciąg 32 bitów)
    :param arg: Argument, dla którego liczymy wartość (zapisany binarnie jako ciąg 32 bitów)
    :return: Wynik działania operacji SBox (Punkt 4. w specyfikacji algorytmu)
    """
    arg_1, arg_2, arg_3, arg_4 = arg[0:8], arg[8:16], arg[16:24], arg[24:32]
    arg_1, arg_2, arg_3, arg_4 = int(arg_1, 2), int(arg_2, 2), int(arg_3, 2), int(arg_4, 2)
    div_1, div_2, div_3, div_4 = arg_1 % 3, arg_2 % 3, arg_3 % 3, arg_4 % 3

    pairs = [[arg_1, div_1], [arg_2, div_2], [arg_3, div_3], [arg_4, div_4]]
    res = []
    for pair in pairs:
        if pair[1] == 0:
            val = sboxes.s_box_0[pair[0]]
        elif pair[1] == 1:
            val = sboxes.s_box_1[pair[0]]
        elif pair[1] == 2:
            val = sboxes.s_box_2[pair[0]]
        res.append(val)

    return "".join(["{0.08b}".format(el) for el in res])
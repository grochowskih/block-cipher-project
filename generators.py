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
        left = int(left, 2) << round
        right = int(right, 2) >> round
    else:
        left = int(left, 2) >> round
        right = int(right, 2) << round

    return "{0:032b}".format(left ^ right)


def s_box(round_key, arg):
    """
    Funkcja, która wybiera w zależności od klucza rundowego odpowiednie SBoxy i wylicza wartość funkcji.
    :param round_key: Klucz rundowy (zapisany binarnie jako ciąg 32 bitów)
    :param arg: Argument, dla którego liczymy wartość (zapisany binarnie jako ciąg 32 bitów)
    :return: Wynik działania operacji SBox (Punkt 4. w specyfikacji algorytmu)
    """
    arg_1, arg_2, arg_3, arg_4 = round_key[0:8], round_key[8:16], round_key[16:24], round_key[24:32]
    arg_1, arg_2, arg_3, arg_4 = int(arg_1, 2), int(arg_2, 2), int(arg_3, 2), int(arg_4, 2)
    div_1, div_2, div_3, div_4 = arg_1 % 3, arg_2 % 3, arg_3 % 3, arg_4 % 3

    pairs = [[arg[0:8], div_1], [arg[8:16], div_2], [arg[16:24], div_3], [arg[24:32], div_4]]
    res = []
    for pair in pairs:
        if pair[1] == 0:
            val = sboxes.s_box_0[int(pair[0], 2)]
        elif pair[1] == 1:
            val = sboxes.s_box_1[int(pair[0], 2)]
        elif pair[1] == 2:
            val = sboxes.s_box_2[int(pair[0], 2)]
        res.append(val)

    return "".join(["{0:08b}".format(el) for el in res])

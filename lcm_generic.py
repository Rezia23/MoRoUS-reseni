def multiple(lcm,rest,tuplet,tuplet_rest):
    global counter
    global common_multiple
    if ((lcm+rest)% tuplet == tuplet_rest):
        print("Mozny pocet robotu je: ", lcm + rest)
        if(counter < 1):    #najde prvni dva nasobky, v prikladu 1.2 neni potreba, protoze se hleda jen nejmensi
            counter +=1
            multiple(lcm+common_multiple,rest,tuplet,tuplet_rest)

    else:
        multiple(lcm+common_multiple,rest,tuplet,tuplet_rest)

common_multiple = 21    #nejmensi spolecny nasobek cisel n z n-tic se stejnym zbytkem
residue = 2             #stejny zbytek
tuplet = 5              #n z n-tice s lisicim se zbytkem
tuplet_rest = 3         #zbytek lisiciho se n
counter = 0             #slouzi k pocitani poctu hledanych nasobku
multiple(common_multiple,residue,tuplet,tuplet_rest)

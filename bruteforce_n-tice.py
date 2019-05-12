
def bruteforce(tuplet,rest):
    global suma
    if (suma%int(tuplet)==rest):
        return True
    else:
        return False

def iterate_dictionary(dictionary):
    for key in dictionary:
        is_result = bruteforce(key,dictionary[key])
        if (is_result == False):
            increasesum(dictionary)
            return
    if (is_result):
        print("Nejmensi mozny pocet je: ", suma)
        return

def increasesum(dictionary):
    global suma
    suma +=1
    iterate_dictionary(dictionary)

dictionary = {"2":1,"3":2,"5":4}    #slovnik hodnot pri deleni robotu - klic je n z n-tice, na ktere se rozdelovali, hodnota je zbytek
suma = 0
increasesum(dictionary)

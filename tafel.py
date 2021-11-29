getal =input('van welke getal wilt u de tafel zien? ')

def tafel(nummer):
    # print(nummer)
    for t in range(1, 11):
        print(nummer * t)
tafel(int(getal))
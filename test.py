from random import randrange


def szamBekeres():
    allitas = True
    try:
        while allitas:
            bekertszam = int(input("Kérek egy 4nél nagyobb számot:"))
            if bekertszam > 4:
                allitas = False
                return bekertszam

    except ValueError as error:
        print(f"Error: {error}")


def tombGeneralas(bekertszam, lst):
    i = 1
    j = 0
    elsoveletlen = randrange(1, bekertszam + 1)
    lst.append(elsoveletlen)

    while i != bekertszam:
        veletlen = randrange(1, bekertszam + 1)

        if veletlen not in lst:
            if i == bekertszam - 1:
                lst.append(veletlen)
                break

            if lst[j] - veletlen >= 2 or veletlen - lst[j] >= 2:
                lst.append(veletlen)
                j = i
                i += 1


def feladat(szaminput, lst):
    tombGeneralas(szaminput, lst)
    for i in range(len(lst)):
        if i == 0:
            continue
        if lst[i - 1] - lst[i] == -1 or lst[i - 1] - lst[i] == 1:
            return
        else:
            return lst

def main():
    ls = []
    szam = szamBekeres()
    feladat(szam, ls)
    print(ls)


if __name__ == "__main__":
    main()
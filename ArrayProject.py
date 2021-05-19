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


def tombGeneralas(bekertszam):
    ls = []

    i = 0
    while i < bekertszam:
        veletlen = randrange(1, bekertszam + 1)
        if veletlen not in ls:
            ls.append(veletlen)
            i += 1
    return ls


def Solution(szambe):
    uncorrect = False
    lst = tombGeneralas(szambe)
    for i in range(len(lst)):
        if i == 0:
            continue
        if lst[i - 1] - lst[i] == 1 or lst[i - 1] - lst[i] == -1:
            uncorrect = True
            break

    if uncorrect == True:
        Solution(szambe)
    else:
        print(lst)


def main():
    szam = szamBekeres()
    Solution(szam)


if __name__ == "__main__":
    main()
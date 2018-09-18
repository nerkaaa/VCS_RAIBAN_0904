import random
import picture
import collections


top_zodziai = open("zodziai.txt", "r")
min_lenght = min(top_zodziai, key=len)

top_zodziai = open("zodziai.txt", "r")
max_lenght = max(top_zodziai, key=len)

# print(len(min_lenght), len(max_lenght))

top_zodziai = open("zodziai.txt", "r")
zodziu_sarasas = []
k = True
while k:

    atspetu_raidziu_sarasas = []
    spetu_zodziu_sarasas = []

    # Start --> Error handling
    while True:
        try:
            lygis = int(input("Pasirinkite Lygį (3-" + str(len(max_lenght)) + "): "))
            break
        except ValueError:
            print("Įveskite skaičių!")
    # End --> Error handling

    while int(lygis) <= 2 or int(lygis) >= len(max_lenght) + 1:
        lygis = int(input("Pasirinkite Lygį (3-" + str(len(max_lenght)) + "): "))

    # Išveda visus rastus elementus pvz.:7
    sk2 = str(len(picture.HANGMANPICS))
    # print(sk2)

    # Start --> Error handling
    while True:
        try:
            klaidu_skaicius = int(input("Pasirinkite kiek galėsite padaryti klaidų (2-" + sk2 + "): "))
            break
        except ValueError:
            print("Įveskite skaičių!")
    # End --> Error handling

    while int(klaidu_skaicius) <= 1 or int(klaidu_skaicius) >= int(sk2) + 1:
        klaidu_skaicius = int(input("Pasirinkite kiek galėsite padaryti klaidų (2-" + sk2 + "): "))

    # print(len(picture.HANGMANPICS))
    sk = len(picture.HANGMANPICS) - klaidu_skaicius

    for zodis in top_zodziai.readlines():
        zodzio_ilgis = zodis.__len__()
        if int(lygis) >= int(zodzio_ilgis):
            zodziu_sarasas.append(zodis.replace("\n", ""))

    # print(zodziu_sarasas)
    zodis = random.choice(zodziu_sarasas)

    # answer first object in the list
    # zodis = zodziu_sarasas[0]
    # administration 14

    # zodis = list(zodziu_sarasas[0])
    # ['a', 'd', 'm', 'i', 'n', 'i', 's', 't', 'r', 'a', 't', 'i', 'o', 'n'] 14

    # Atsakymas
    # print(zodis, len(zodis), "\n")

    linijos = []
    linijos.extend(zodis)

    # klaidos = int(klaidu_skaicius)
    # print(klaidos)

    for i in range(len(linijos)):
        linijos[i] = "-"

    print("Atspėkite žodį: ")
    print(' '.join(linijos))
    print("\n")

    x = 0
    klaidos = 0
    s = int(len(zodis) + klaidu_skaicius)

    while klaidu_skaicius != klaidos:

        # print("---> Kartai:", x, "Klaidos:", klaidos, "Spejimai:", s)
        # Start --> Error handling
        while True:
            try:
                spejimas = str(input("Įrašykite raidę: "))
                if spejimas.isalpha():
                    break
            except ValueError:
                print("Ups..galimos tik raidės!")
        # End --> Error handling

        if spejimas == "stop":
            pasirinkimas = input("Ar norite tęsti žaidimą ( y / n )?\n")
            if pasirinkimas == "n":
                print("Iki greito...")
                break
            else:
                continue

        for i in range(len(zodis)):
            if zodis[i] == spejimas:
                linijos[i] = spejimas

        print(' '.join(linijos))
        print("\n")

        if spejimas in zodis:
            atspetu_raidziu_sarasas.append(spejimas)
            counters = collections.Counter(atspetu_raidziu_sarasas)
            for e in counters.items():
                if e[0] == spejimas and e[1] > 1:
                    print(picture.HANGMANPICS[sk])
                    klaidos += 1
                    print("Raidė jau spėta!. Iš viso klaidų:", klaidos)
                    sk += 1

        if spejimas not in zodis:  # Linas
            # raide pridedama i sarasa
            spetu_zodziu_sarasas.append(spejimas)
            # sakiciuojamos pasikartojancios raides
            counter = collections.Counter(spetu_zodziu_sarasas)
            for a in counter.items():
                if a[0] == spejimas and a[1] == 2:
                    print("Papildomas spėjimas")
                    # print("Spėtų žodžių sąrašas:", spetu_zodziu_sarasas)
                    # print("Padarėte klaidą. Viso:", klaidos)
                    # print("Zodziu skaciavimas: ", counter)
                    klaidos += 0

                if a[0] == spejimas and a[1] == 1:
                    print(picture.HANGMANPICS[sk])
                    klaidos += 1
                    print("Padarėte klaidą. Viso klaidų:", klaidos)
                    sk += 1

                if a[0] == spejimas and a[1] > 2:
                    print(picture.HANGMANPICS[sk])
                    klaidos += 1
                    print("Raidė jau spėta!. Iš viso klaidų:", klaidos)
                    sk += 1

        if klaidu_skaicius == klaidos:
            print("\nTeisingos raidės:", atspetu_raidziu_sarasas)
            print("\nKlaidingos raidės:", spetu_zodziu_sarasas)
            print("\nPadarėte visas", klaidu_skaicius, "galimas klaidas! Deja, žaidimas baigtas... :(")
            break

        if "-" not in linijos:  # Linas
            # print(spetu_zodziu_sarasas)
            print("\nSveikiname su pergale. Ar bandysite dar karta?")
            break
        x += 1
        s -= 1

    ats = input("\nAr norite žaisti iš naujo ( y / n )?\n")
    if ats == "y":
        k = True
    else:
        print("Ačiū, kad žaidėte... :)")
        k = False

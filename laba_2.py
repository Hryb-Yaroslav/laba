alf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
a = input("Введіть дію a/b: ")
if a == "a":
    b = input().lower()
    for i in alf:
        c = 0
        w = ""
        for j in b:
            if i == j:
                c += 1
                e = str(c)
                w = i+" "+e
        if w != "":
            print(w)
if a == "b":
    s = []
    b = input().lower().split(" ")
    for i in b:
        c = len(i)
        if c <= 3:
            continue
        d = ""
        for j in i:
            if j == "," or j == ":" or j == " " or j == ";" or j == ".":
                continue
            d = d+j
        if d not in s:
            s.append(d)
    for o in sorted(s):
        print(o)

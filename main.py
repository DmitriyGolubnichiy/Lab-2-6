
x = []
def WriteKvadratList(x):
    end = ""

    while end != "end":
        a = int(input())
        if a ** 2 < 30:
            x.append(a)
        elif a == 254:
            end = "end"
        else:
            continue

    return (x)

WriteKvadratList(x)

with open("DlyaZapisi.txt", 'w') as File:

    print(x, file=File)

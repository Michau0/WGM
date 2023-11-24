from PIL import Image

obraz = Image.open("obraz.jpg")

def rysuj_kwadrat_max(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp=[0,0,0]
    temp_max=[0,0,0]

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]

            temp[0] = pixel[0]
            temp[1] = pixel[1]
            temp[2] = pixel[2]

            for i in range(3):
                if temp[i] > temp_max[i]:
                    temp_max[i] = temp[i]

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d

            pix1[x, y] = (temp_max[0], temp_max[1], temp_max[2])

    return obraz1


def rysuj_kwadrat_min(obraz, m, n, k):
    obraz2 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz2.load()
    d = int(k / 2)
    temp=[0,0,0]
    temp_min=[255,255,255]

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]

            temp[0] = pixel[0]
            temp[1] = pixel[1]
            temp[2] = pixel[2]

            for i in range(3):
                if temp[i] < temp_min[i]:
                    temp_min[i] = temp[i]

    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d

            pix1[x, y] = (temp_min[0], temp_min[1], temp_min[2])

    return obraz2




obraz1_1 = rysuj_kwadrat_max(obraz, 60, 170, 25)
obraz1_1 = rysuj_kwadrat_max(obraz1_1, 100, 50, 15)
obraz1_1 = rysuj_kwadrat_max(obraz1_1, 120, 300, 35)

obraz1_1.show()


obraz2_1 = rysuj_kwadrat_min(obraz, 60, 170, 25)
obraz2_1 = rysuj_kwadrat_min(obraz2_1, 100, 50, 15)
obraz2_1 = rysuj_kwadrat_min(obraz2_1, 120, 300, 35)

obraz2_1.show()


def rysuj_kolo_kopiuj(obraz, m_s, n_s, r, m_src, n_src):
    obraz3 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz3.load()
    w, h = obraz.size

    for i in range(w):
        for j in range(h):
            if (i - m_src) ** 2 + (j - n_src) ** 2 < r ** 2:
                pix1[i + m_s, j + n_s] = pix[i, j]


    return obraz3

obraz3_1 = rysuj_kolo_kopiuj(obraz, 100, 200, 25, 300, 100)
obraz3_1.show()


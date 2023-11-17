from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

obraz = Image.open("obraz.jpg")
obraz1 = obraz.copy()
obraz2 = obraz.copy()
obraz3 = obraz.copy()
obraz4 = obraz.copy()
inicjaly = Image.open("inicjaly.bmp")

def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]

def wstaw_inicjaly(obraz, incijaly, m, n, kolor):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if incijaly.getpixel((i, j)) == 0:
                obraz.putpixel((i + m, j + n), kolor)
    return obraz

kolor = (250, 0, 0)

obraz1 = wstaw_inicjaly(obraz1, inicjaly, 710, 410, kolor)
obraz1.save("obraz1.jpg")


def wstaw_inicjaly_maska(obraz, maska, m, n, x, y, z):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    w, h = obraz.size
    w0, h0 = maska.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if maska.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    return obraz


obraz2 = wstaw_inicjaly_maska(obraz, inicjaly, 300, 300, 255, 50, 100)
obraz2.save("obraz2.jpg")


def wstaw_inicjaly_load(obraz, inicjaly, m, n, a, b, c):
    w, h = obraz.size
    w0, h0 = inicjaly.size
    inicjaly_load = inicjaly.load()
    obraz_load = obraz.load
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly_load[i, j] == 0:
                obraz_load[i + m, j + n] = (a, b, c)
    return obraz


obraz3 = wstaw_inicjaly_load(obraz4, inicjaly, 50, 50, 255, 0, 0)
obraz3.save("obraz3.jpg")
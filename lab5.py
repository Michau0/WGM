from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

obraz1 = Image.open('diff.png')


def statystyki(obraz1):
    s = stat.Stat(obraz1)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

statystyki(obraz1)

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.savefig("histogram1.png")
    plt.show()



rysuj_histogram_RGB(obraz1)

def zlicz_roznice_srednia_RGB(obraz, wsp):  # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if np.mean(t_obraz[i, j, :]) > wsp:
                zlicz = zlicz + 1
    procent = zlicz / (h * w)
    return zlicz, procent


def zlicz_roznice_suma_RGB(obraz, wsp):  # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
            if sum(t_obraz[i, j, :]) > wsp:
                zlicz = zlicz + 1
    procent = zlicz / (h * w)
    return zlicz, procent


zlicz1, procent1 = zlicz_roznice_srednia_RGB(obraz1, 10)
zlicz2, procent2 = zlicz_roznice_srednia_RGB(obraz1, 8)
zlicz3, procent3 = zlicz_roznice_srednia_RGB(obraz1, 3)


print('liczba niepasujących pikseli = ' , zlicz1)
print('procent niepasujących pikseli = ' , procent1)

print('liczba niepasujących pikseli = ' , zlicz2)
print('procent niepasujących pikseli = ' , procent2)

print('liczba niepasujących pikseli = ' , zlicz3)
print('procent niepasujących pikseli = ' , procent3)
# coding: utf-8

"""
    OpenCV ile goruntu isleme
    @author: Yunus Emre
    @date: 2018
"""

# OpenCV (goruntu isleme) dahil etme
import cv2

# Gelimis matrix ve matematiki islemlerini icerir
import numpy as np

# Arc tan
from math import atan;

# # Koordinat sisteminde resmi cizdirmek icin kullanilir
# import matplotlib.pyplot as plt

def kenarlari_bul(resim):
    """
        Resimdeki kenarlari bulma ve dondurme

        Parameters
        ----------
        resim : Kenarlari bulunacak resim
    """
    # Renk filtresi ekleme
    gri_filtre = cv2.cvtColor(resim, cv2.COLOR_RGB2GRAY)
    # Resme bulaniklik ve filtre ekleme (filtre, ortalama alma alani (5x5 matrix))
    bulaniklik = cv2.GaussianBlur(gri_filtre, (5, 5), 0)
    # Canny kenar bulma yonetemi ile kesnar bulma
    return cv2.Canny(bulaniklik, 50, 150)


def ilgi_alanini_ayarla(resim):
    """
        Resmin ilgi alanina gore maskeler

        Parameters
        ----------
        resim : Maskelenecek resim
    """
    # Resmin yuksekligini alma
    yukseklik = resim.shape[0]
    # Ele alinacak ucgensel alani olusturma ([A, B, C noktalari])
    ucgen = np.array([(200, yukseklik), (1100, yukseklik), (550, 250)])
    # Resmi maskelemek icin onunla ayni olan 0 matrixi olusturuyoruz
    maske = np.zeros_like(resim)

    # Maskeleme islemi
    # Not: Maskeleme islemi icin birden fazla cokgen gerektiginden dizi yapiyoruz []
    cv2.fillPoly(maske, [(ucgen)], 255)

    maskelenmis_resim = cv2.bitwise_and(resim, maske)

    # Maskeyi dondurme
    return maskelenmis_resim


def cizgileri_goster(resim, cizgiler):
    # Resme es deper bir kalip olusturuyoruz
    resmin_cizgileri = np.zeros_like(resim)

    # Eger cizgiler dizisi bos degilse
    if cizgiler is not None:
        # Her bir cizgiyi ele alma
        for cizgi in cizgiler:
            # cizgi 4 tane noktadan olusmak zorundadir
            if len(cizgi) == 4:
                # 2D diziyi, 1D 4 sutundan olusan diziye ceviriyoruz ve her elamani atiyoruz
                x1, y1, x2, y2 = cizgi

                # Resmin cizgilerini olusturma
                # resim, P1, P2, BRG, cizgi kalinligi
                cv2.line(resmin_cizgileri, (x1, y1), (x2, y2), (255, 0, 0), 10)

    return resmin_cizgileri


def koordinatlari_ayarla(resim, cizgi_parametreleri):
    """
        cizginin koordinatlarini ayarlama

        Parameter
        ----------
        resim : array_like
            Resim dizisi
        cizgi_parametreleri : tuple, array
            F = mx + n'deki (m, n) verileri
    """

    # cizgi parametrelerini alma
    m, n = cizgi_parametreleri

    # Resmin yuksekligi tabaninin y koordinatini verir
    y1 = resim.shape[0]
    # Resmin sadece 2 / 5 'ini ele alacagimizdan (5 - 2 = 3) y2'i ayarliyoruz
    y2 = int(y1 * (3 / 5))

    # y = mx + n -> x = (y - n) / m
    x1 = int((y1 - n) / m)
    x2 = int((y2 - n) / m)

    # Sonucu cigi verisi olorak 1D dondurme
    return np.array([x1, y1, x2, y2])


def cizgileri_duzelt(resim, cizgiler):
    """
        cizgileri duzeltme
    """
    # Sol taraftaki cizgi
    sol_cizgi = []

    # Sag taraftaki cizgi
    sag_cizgi = []

    
    if cizgiler is not None:
        # Her bir cizgiyi isleme
        for cizgi in cizgiler:
            # 2D den 1D'ye cekme
            x1, y1, x2, y2 = cizgi.reshape(4)

            # 2 noktasi bilinen dogrunun verilerini bulma (mx + n)
            parametreler = np.polyfit((x1, x2), (y1, y2), 1)

            # Egim
            m = parametreler[0]
            # Sabit sayi
            n = parametreler[1]

            # Eger aci negatif ise solda pozitif sagda olan cizgiyi ele alir
            if m < 0:
                sol_cizgi.append((m, n))
            else:
                sag_cizgi.append((m, n))

        # Eger solda cizgi varsa isleme
        if len(sol_cizgi) > 0:
            # Ortalamalari hesaplama
            sol_cizgi_ortalamasi = np.average(sol_cizgi, axis=0)
            # Ortalamalar ile duzgun cizgi koordinatlarini bulma
            sol_cizgi = koordinatlari_ayarla(resim, sol_cizgi_ortalamasi)

        # Eger sagda cizgi varsa isleme
        if len(sag_cizgi) > 0:
            # Ortalamalari hesaplama
            sag_cizgi_ortalamasi = np.average(sag_cizgi, axis=0)
            # Ortalamalar ile duzgun cizgi koordinatlarini bulma
            sag_cizgi = koordinatlari_ayarla(resim, sag_cizgi_ortalamasi)
        
    # Duzgun cizgi verilerini geri dondurme
    return np.array([sol_cizgi, sag_cizgi])

def donus_acisini_hesapla(çizgiler):
    sol_cizgi, sag_cizgi = çizgiler
    #  Orta çizgiyi bulma
    orta_cizgi = ((sol_cizgi + sag_cizgi) / 2).astype(int)

    # Dönüş açınsı hesaplama
    # + sağ
    # - sol
    x0, y0, x1, y1 = orta_cizgi
    donus_acisi = 90 - atan((y1 - y0) / (x1 - x0))
    donus_acisi /= 90

    return donus_acisi


def seritleri_bul(resim):
    # Resmi matrix'e cevirme. (Resim ismi turkce karakter iceremez)
    # resim = cv2.imread(resim_yolu)

    # resim_cizgileri = resim yaparsak 2si birbirine esdeger olur, orjinal resim degsir
    # orjinal resim degismesin diye, kopyasini yollamamiz gerekmekte
    kopya_resim = np.copy(resim)

    # Resmi kenarlara odakli hale getiriyoruz
    kenarli_resim = kenarlari_bul(kopya_resim)

    # # Koordinat sisteminde resmi gostermek icin hazirlama
    # plt.imshow(kenarlari_bul(kopya_resim))
    # # Resmi gorunur kilma
    # plt.show()

    # İlgi alanina odakli resim haline getiriyoruz
    odaklanmis_resim = ilgi_alanini_ayarla(kenarli_resim)

    # cizgileri belirleme
    cizgiler = cv2.HoughLinesP(
        odaklanmis_resim, 2, np.pi / 180, 100,
        np.array([]), minLineLength=40, maxLineGap=5
    )

    # Resmin cizgilerini duzgun ve kisa hale getirme
    duzeltilmis_cizgiler = cizgileri_duzelt(kopya_resim, cizgiler)

    # Dönüş açınısını hesaplama
    dönüş_açışı = donus_acisini_hesapla(duzeltilmis_cizgiler);

    # Resmin cizgilerini siyah ekranda gosterme
    resmin_cizgileri = cizgileri_goster(kopya_resim, duzeltilmis_cizgiler)

    # Resmin cizgilerini orjinal resmin kopyasi uzerine ekleme
    # kopya resim, yogunlugu, cizgileri, yogunlugu, gama degeri [parlaklik denebilir] (toplana eklenecek deger)
    cizgili_resim = cv2.addWeighted(kopya_resim, 0.8, resmin_cizgileri, 1, 1)

    # Resmi gosterme alanini acma
    cv2.imshow("result", cizgili_resim)
    # Resmin kac ms gosterilecegi
    return cv2.waitKey(1)


def video_seritlerini_bul(video_yolu, cikis_karakteri="q"):
    # Video yakalama islemi
    cap = cv2.VideoCapture(video_yolu)

    # Video oynatildigi surece bu islemleri yapacagiz
    while (cap.isOpened()):
        # Videodaki her resmi ele alma
        # İlk veri booleandir, ele almiyoruz. 2. veri resimdir
        _, video_karesi = cap.read()

        # Eger video karesi alinamazsa veya cikis karakteri girilirse kapatma
        if video_karesi is None or seritleri_bul(video_karesi) == ord(cikis_karakteri):
            break

    cap.release()
    cv2.destroyAllWindows()

video_seritlerini_bul("test.mp4")

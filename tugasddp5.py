# -*- coding: utf-8 -*-
"""tugasDDP5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17XUtmX1S8BJ7PLnhpK1K_ZbxavZad56s
"""

#soal no 1
kendaraan=["mobil","matic","1497cc","putih","4"]
print(kendaraan)
kendaraan.append("RS AT")
kendaraan.append("210.000.000")
kendaraan.insert(2,"honda jazz")
print(kendaraan)

#soal no 2
pilihan = int(input("masukkan pilihan : "))
persegi = ("luas perseg adalahi : ")
lingkaran = ("luas lingkaran adalah : ")
segitiga = ("luas segitiga adalah : ")

match pilihan:
    case 1:
        print(persegi, int(input("sisi: ")) **2)
    case 2:
        print(lingkaran, 3.14* float(input("masukkan jari-jari : "))**2)
    case 3:
        print(segitiga, 0.5* float(input("masukkan panjang alas: "))* float(input("masukkan tinggi alas: ")))
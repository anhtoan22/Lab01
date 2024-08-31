# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:03:33 2024

@author: Huỳnh Anh Toàn - 23705641
"""
gio = float(input("Nhập giờ: "))
phut = float(input("Nhập phút: "))
giay = float(input("Nhập giây: "))
if (0<gio<23) and (0<=phut<60) and (0<=giay<60):
    print ("Hợp lệ")
else:
    print ("Không hợp lệ")

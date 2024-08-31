# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:12:17 2024

@author: Huỳnh Anh Toàn - 23705641
"""
char = input("Nhập vào một chữ cái hoa hoặc thường: ")
if char.islower():
    chu_hoa = char.upper()
    print(f"{char} là: {chu_hoa}")
else:
    chu_thuong = char.lower()
    print(f"{char} là: {chu_thuong}")

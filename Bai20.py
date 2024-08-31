# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:25:04 2024

@author: Huỳnh Anh Toàn - 23705641
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
if a>b:
    b=a
if b>c:
    c=b
print(f"Số lớn nhất là: {c}")
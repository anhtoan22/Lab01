# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:18:35 2024

@author: Huỳnh Anh Toàn - 23705641
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
if a < b:
    b = a
if b < c:
    c = b
if c < d:
    d = c
print(f"Số nhỏ nhất là: {d}")

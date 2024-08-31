# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:54:03 2024

@author: Huỳnh Anh Toàn - 23705641
"""
thoi_gian = input("Nhập vào thời gian (..h..p..s): ")
so = ""
for i in thoi_gian:
    if i.isalpha():
        so += ":"
    else:
        so += i
final_so = so[:-1]
h, p, s = map(int, final_so.split(':'))
giay = h * 3600 + p * 60 + s
print("Thời gian là (s):", giay)
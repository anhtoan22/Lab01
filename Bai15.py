# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:51:48 2024

@author: Huỳnh Anh Toàn - 23705641
"""
a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
ve_dau = ((a + b) / (a ** (1/3) + b ** (1/3))) - ((a * b) ** (1 / 3))
ve_sau = (a ** (1/3) - b ** (1/3)) ** 2
dap_an = (ve_dau / ve_sau)
print("Kết quả biểu thức là: ", dap_an)

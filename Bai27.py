# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:25:11 2024

@author: Huỳnh Anh Toàn - 23705641
"""
import math
hinh = input("Nhập hình (vuông, chữ nhật, tròn): ")
if hinh == 'vuông':
    canh = float(input("Nhập số đo cạnh: "))
    S=canh*canh
    P=canh*4
print (f"Chu vi {P} diện tích {S}")
if hinh == 'chữ nhật':
    dai = float(input("Nhập số đo chiều dài: "))
    rong = float(input("Nhập số đo chiều dài: "))
    S=dai*rong
    P=(dai+rong)*2
print (f"Chu vi {P} diện tích {S}")
if hinh == 'hình tròn':
    r = float(input("Bán kính: "))
    P=2*3.14*r
    S=3.14*r**2
print (f"Chu vi {P} diện tích {S}")




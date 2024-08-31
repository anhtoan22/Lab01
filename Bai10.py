# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:38:23 2024

@author: Huỳnh Anh Toàn - 23705641
"""
so_xe = input("Nhập số xe (4 chữ số): ")
if len(so_xe)!=4 :
    print("Số xe phải là 4 chữ số.")
else:  
    tong = sum(int(chu_so) for chu_so in so_xe)
    so_nut = tong % 10
    print("Số nút của số xe {so_xe} là: ", so_nut)

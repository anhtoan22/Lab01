# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:36:21 2024

@author: Huỳnh Anh Toàn - 23705641
"""
a = float(input("Nhập vào giá trị của a: ")) 
b = float(input("Nhập vào giá trị của b: ")) 
phuong_trinh = f"Phương trình bậc nhất {a}x + {b} = 0"
if a == 0:
    if b == 0:
        print(f"{phuong_trinh} có vô số nghiệm")
    else:
        print(f"{phuong_trinh} vô nghiệm")
else:
    x = (-b) / a
    print(f"{phuong_trinh} có nghiệm: {x}")

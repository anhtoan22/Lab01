# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:40:23 2024

@author: Huỳnh Anh Toàn - 23705641
"""
a = float(input("Nhập vào giá trị của a: ")) 
b = float(input("Nhập vào giá trị của b: ")) 
c = float(input("Nhập vào giá trị của c: ")) 
phuong_trinh=f"Phương trình bậc hai {a}x**2 + {b}x + {c} = 0"
delta = b**2 - 4*a*c 
if delta < 0:
    print (f"{phuong_trinh} vô nghiệm")
elif delta == 0:
    print (f"{phuong_trinh} có 2 nghiệm kép là: -{c}/2*{a}")
elif a==0:
    print (f"{phuong_trinh} có nghiệm: -{c}/{b}")
else:
    print (f"{phuong_trinh} có 2 nghiệm phân biệt là: [-{b} + math.sqrt(delta)]/2*{a} và [-{b} - math.sqrt(delta)]/2*{a}")

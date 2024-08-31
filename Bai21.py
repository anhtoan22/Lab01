# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:28:54 2024

@author: Huỳnh Anh Toàn - 23705641
"""
chu_so = int(input("Nhập một số: "))
doc = {0:'Khong', 1:'Mot', 2:'Hai', 3:'Ba', 4:'Bon', 5:'Nam', 6:'Sau', 7:'Bay', 8:'Tam', 9:'Chin'}
if chu_so >= 0 and chu_so <= 9:
    chu_so = doc.get(chu_so)
    print(chu_so)
else:
    print("Khong doc duoc")
    
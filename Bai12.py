# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:40:34 2024

@author: Huỳnh Anh Toàn - 23705641
"""
import random
integer_ranges = [(0, 100),(50, 100),(-39, 79),(-79, -39)]
float_ranges = [(0, 100),(50, 100),(-39, 79),(-79, -39)]
for start, end in integer_ranges:
    print(f"Số nguyên ngẫu nhiên từ {start} đến {end}: {random.randint(start, end)}")
for start, end in float_ranges:
    print(f"Số thực ngẫu nhiên từ {start} đến {end}: {round(random.uniform(start, end), 2)}")

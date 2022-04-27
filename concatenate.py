# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:40:45 2022

@author: Ludving Cano

CONCATENATE VER. 0.1
"""

import os
import re

import time
start_time = time.time()

orig_data_path = "D:\\LFA\\LIDAR_Code\\"
ls = os.listdir(orig_data_path)

r = re.compile("^\d{4}_\d{2}_\d{2}")
ls = list(filter(r.match, ls))

print("¿Cuál carpeta usar?")
for i, j in enumerate(ls):
    print(j, ".....", i)

#selection = int(input("Ingrese número: "))
selection = 0
selection = ls[selection]
new_path = orig_data_path + selection + "\\"
new_ls = os.listdir(new_path)

r = re.compile("\d{2}_\d{2}_\d{2}_HR\d{4}_\d{2}.ch1.txt")
ls = list(filter(r.match, new_ls))

qtn = len(ls)
print("Se encontraron", qtn, "archivos")

new_file = ""
for i in ls:
    file_path = new_path + i
    with open(file_path, "r") as file:
        ff = file.read()
        ff = ff.replace(",", ".")
    new_file = new_file + ff + "\n"
    
raw_path = "D:\\LFA\\LIDAR_Code\\raw_data\\result.txt"
with open(raw_path, "w+") as file:
    file.write(new_file)
    
print("--- %s seconds ---" % (time.time() - start_time))
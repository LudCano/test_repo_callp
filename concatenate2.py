# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:40:45 2022

@author: Ludving Cano

CONCATENATE VER. 0.1
"""

import os
import re
import pandas as pd

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
ff = []
for i in ls:
    file_path = new_path + i
    file = open(file_path)
    for line in file:
        lst = []
        line = line.replace(",", ".")
        """
        dat = np.array(line.split())
        dat = dat.astype(float)
        for i in range(2):
            dat[i] = dat[i].astype(int)
        """
        for j in line.split():
            lst.append(float(j))
        lst[0] = int(lst[0])
        lst[1] = int(lst[1])
        lst[2] = round(lst[2],3)
        ff.append(lst)
        del(lst)
        
df = pd.DataFrame(ff)
del(ff)
df.to_csv('filename.txt', sep='\t', index=False, header = False)


print("--- %s seconds ---" % (time.time() - start_time))
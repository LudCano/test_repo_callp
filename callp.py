###########################################################################
#                   COMPLETE ANALYSIS FOR LIDAR DATA IN LA PAZ
# 
# This program tries to get together all the possible information that lidar 
# data can gives you. All the functions used in this program were developed,
# improved and tested by the Laboratory for Atmospheric Physics, Lalinet and  
# Matlab during 2012-2018. 
#
#                           ~ IMPORTANT~ 
#      1. The files that you can use for this program are the ones that are
#         already concatenated. 
#      2. Remember that each day of data is different, so lidar data can't 
#         be treated fully automatically, you may have some problems when 
#         generalizing parameters. 
#         
#
# author: 
# Ludving Cano Fernandez (lcano@chacaltaya.edu.bo)
# based on the code written on Matlab by:
# Lic. Maria Fernanda Sanchez (mafer.sb@chacaltaya.edu.bo)
#
# version 1.0 >> 12/04/2018
# version 1.1 >> 16/06/2019  (automatic export of figures)     
###########################################################################


#+ 1. IMPORT DATA
#+ For this part you can select a range of dates or only 1 day of data.
print("1. IMPORT THE DATA")
from import_data import import_data
path = "/home/ludving/PROJ/LFA/LIDAR_Code/raw_data" #¿ Donde se encuentran los datos concatenados
folder = "/home/ludving/PROJ/LFA/LIDAR_Code/" #¿ Se encuentran las carpetas de los datos
[FileName, PathName, dates_import, data] = import_data(path)

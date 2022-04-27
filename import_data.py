#
#+ ######################################################################
#+                       FUNCTION IMPORT_DATA
#+ With this function you are able to select all the data that you need,
#+ even if you don't know exactly what days to import.
#+
#+ Input:
#+ path....... This is the folder where are all the raw data concatenated
#+ 
#+ Outputs:
#+ f_names ........ List of the names of the files imported
#+ f_paths ........ Tuple of the paths of the files imported
#+ dates_import ... List of info (year, month, day, angle) about dates imported
#+ data ........... NumPy array of data imported, must be handled carefully as this variable is big
#+
#+ Author: Ludving Cano Fernandez     lcano@chacaltaya.edu.bo
#+ Based on the code written on Matlab by Lic. Maria Fernanda Sanchez Barrero
#+ mafer.sb@chacaltaya.edu.bo
#+ #######################################################################

import numpy as np
import tkinter
from tkinter import filedialog
from matplotlib import dates
import pandas as pd
import re

def import_data(path):
    """
    You can select the files which you want to import to run CALLP,
    returns information about those files and the data imported

    Parameters
    ----------
    path : str
        Location where raw files are located

    Returns
    -------
    f_names : List of strings
        List of the names of the files imported
    f_paths : Tuple of strings
        Tuple of the paths of the files imported
    dates_import : List of tuples
        List of info (year, month, day, angle) about dates imported
    data : np.array
        NumPy array of data imported, must be handled carefully as this variable is big

    """
    path_csv = path + "/datos_lidar1.csv"
    dat = pd.read_csv(path_csv, sep = ";")
    print("Do you already know what date(s) you want to select?")
    ask_select = int(input("YES(1) or NO(0) >> "))
    #ask_select = 1

    #¿ //////////////////////////////////////////////////////////////////
    #¿                  When you know which dates you want
    #¿ //////////////////////////////////////////////////////////////////
    if ask_select == 1:
        #¿ Selecting files and storing them as a list
        root = tkinter.Tk()
        filez = filedialog.askopenfilenames(parent=root, title='Choose a file', filetypes=[("Datos", "*.txt")], initialdir=path)
        
        #¿ Creating the matrix DATES_IMPORT with the data to import
        dates_import = []
        f_names = []
        f_paths = filez
        for i in filez: #¿ Checks if all files are formatted correctly
            reg = path + "/" + "\d{4}_\d{2}_\d{2}_rawdata_[a-zA-Z0-9]{2}.txt"
            r = re.compile(reg)
            if re.match(r, i):
                flg = 0
            else:
                print("ERROR: YOU DIDN'T SELECT A SUPPORTED FILE")
                spli = i.split(sep = "/")
                spli = spli[-1]
                print(spli, "is not a concatenated file")
                quit()

        for i in filez:
            path_splitted = i.split(sep="/")
            filename = path_splitted[-1]
            splited_fname = filename.split(sep = "_")
            year = int(splited_fname[0])
            month = int(splited_fname[1])
            day = int(splited_fname[2])
            angle = int(splited_fname[-1].split(sep=".")[0])
            inf_dat = (year, month, day, angle)
            dates_import.append(inf_dat)
            f_names.append(filename)



    #¿ //////////////////////////////////////////////////////////////////
    #¿                  IMPORTING DATA
    #¿ //////////////////////////////////////////////////////////////////
    #¿ Showing the data to import
    if len(dates_import) == 0:
        print("Definitely, there is no data to import")
    else:
        if len(f_names) > 1:
            print("Wow, more than 1 file selected!")
        print(">> These are the dates that you are going to import <<")
        print("  year  month  day  angle")
        display_dates(dates_import)
        print("Do you want to continue importing the data?")
        cont_process = int(input("YES (1), NO (0) >> "))
        
        if cont_process == 1:
            print("Importing data...")
            for i, j in enumerate(filez):
                if len(f_names) > 1:
                    #¿ Importing multiple files
                    print("Importing ...", f_names[i])
                    if i == 0: #¿ For the first reading we create the data, then we will concat to this array
                        data = np.genfromtxt(j)
                        print("File imported, had a size of", np.shape(data))
                    else: #¿ now we concat to this previous data
                        dat_aux = np.genfromtxt(j)
                        print("File imported, had a size of", np.shape(dat_aux))
                        data = np.concatenate((data, dat_aux), axis = 0)
                else:
                    #¿ Importing only one file
                    print("Importing ...", f_names[i])
                    data = np.genfromtxt(j)
                    print("File imported, size", np.shape(data))
            print("--------------------")
            print("ALL THE DATA THAT YOU NEED IS READY TO USE")
            data_size = np.shape(data)
            print("THE FINAL LENGHT OF DATA IS >>", data_size[0])
        else:
            print("GAME OVER, START AGAIN")
            data = 0

    return f_names, f_paths, dates_import, data

def display_dates(dates_imp):
    """
    Prints the variable dates_import as a sequence of strings

    Parameters
    ----------
    dates_imp : list of tuples
        List of tuples, inside each tuple there must be the format (year, month, day, angle)
        as a form of information of a file

    Returns
    -------
    None.

    """
    for i in dates_imp:
        str_aux = ""
        for j in i:
            str_aux = str_aux + "  " + str(j)
        print(str_aux)


#¿ The following code is only for testing and won't run if we only need the functions from another file
if __name__ == "__main__":  
    concat_path = "/home/ludving/PROJ/LFA/LIDAR_Code/raw_data" #¿ Donde se encuentran los datos concatenados
    folder = "/home/ludving/PROJ/LFA/LIDAR_Code/" #¿ Se encuentran las carpetas de los datos
    a, b, c, d= import_data(concat_path)


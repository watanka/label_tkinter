'C:/Users/신은성/Downloads/6')import os
import glob

def del_dup(main_folder, checking_folder):
    checking=[i for i in os.listdir(checking_folder)]
    for dup in os.listdir(main_folder):
        if dup in checking:
            os.remove(os.path.join(main_folder,os.path.normpath(dup)))

#check: 5&6 on main: 1_2
# check:7&8 on main: 2_3
del_dup('C:/Users/신은성/Downloads/1_2',
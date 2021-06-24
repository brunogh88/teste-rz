from distutils.dir_util import remove_tree
from os import path

def delete_folder(path_folder):
    if path.exists(path_folder):
        remove_tree(path_folder)

def path_exist(path_folder):
    if path.exists(path_folder):
        return True
    else:
        return False

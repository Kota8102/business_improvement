# フォルダ作成モジュール
import os
import shutil

def make_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def clean_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)

if __name__ == "__main__":
    make_folder("./src/temp")
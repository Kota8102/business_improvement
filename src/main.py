import shutil
import glob
from libs import operation_folder as df
from libs import split_pdf as sp
from libs import pdf2txt

import PySimpleGUI as sg

def __init__():
    df.make_folder("./tmp")
    df.make_folder("output")


def main():
    
    __init__()

    search_word = "品質"
    company_name = "スバル"

    inp = "./input/2021_0511_ScV2h_8Rnh.pdf"

    # pdf分割
    sp.split_pdf_pages(inp, "./tmp/temp1")

    files = glob.glob("tmp/*.pdf")
    
    for i in range(len(files)):
        result_txt = pdf2txt.get_txt(files[i])

        if search_word in result_txt:
            shutil.copyfile(files[i], "output/"+company_name+"_ページ_"+str(i)+".pdf")

    # tempフォルダ削除
    df.clean_folder("./tmp")

main()
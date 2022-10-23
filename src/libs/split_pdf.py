from genericpath import exists
import sys
import os
import PyPDF2

def split_pdf_pages(src_path, dst_basepath):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    for i in range(src_pdf.numPages):
        dst_pdf = PyPDF2.PdfFileWriter()
        dst_pdf.addPage(src_pdf.getPage(i))
        with open('{}_{}.pdf'.format(dst_basepath, i), 'wb') as f:
            dst_pdf.write(f)

def main(inp):
    split_pdf_pages(inp, "temp/test1/test1")
    
if __name__ == "__main__":
    sys.exit(main("/workspaces/improvement/save_pdf/2021_0511_ScV2h_8Rnh.pdf"))

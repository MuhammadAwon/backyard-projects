import PyPDF2
import sys

file_name = sys.argv[1:]

def file_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')

file_combiner(file_name)

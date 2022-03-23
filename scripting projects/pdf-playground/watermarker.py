'''Make a tool that can watermark all the given pdfs'''
# import PyPDF2
# from PyPDF2 import PdfFileReader, PdfFileWriter


# inputpdf = PdfFileReader(open('super.pdf', 'rb'))
# waterpdf = PdfFileReader(open('wtr.pdf', 'rb'))
# outputpdf = PdfFileWriter()

# for i in range(inputpdf.getNumPages()):
#     page = inputpdf.getPage(i)
#     page.mergePage(waterpdf.getPage(0))
#     outputpdf.addPage(page)

#     with open('watermarked.pdf', 'wb') as file:
#         outputpdf.write(file)
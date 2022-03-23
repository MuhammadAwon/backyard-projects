# import PyPDF2

# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     rotate = page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(rotate)
#     with open('updown.pdf', 'wb') as file2:
#         writer.write(file2)

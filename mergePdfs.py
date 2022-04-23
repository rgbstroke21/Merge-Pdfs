import os
from PyPDF2 import PdfFileMerger


path = input('Enter the path of folder : ')
pdfs = os.listdir(path)

files = (file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)))

merger = PdfFileMerger()

for file in files:
    print(file)
    merger.append(file)

merger.write("result.pdf")
merger.close()
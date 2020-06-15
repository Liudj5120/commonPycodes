# PDFMerge.py
# 合并pdf文件
from PyPDF2 import PdfFileReader, PdfFileWriter 

def pdfMerge(filepaths, savepath):
    pdfWriter = PdfFileWriter()
    for path in filepaths:
        pdfRader = PdfFileReader(path)
        for page in range(pdfRader.getNumPages()):
            pdfWriter.addPage(pdfRader.getPage(page))
    with open(savepath, 'wb') as out:·
        pdfWriter.write(out)
def main():
    path = r'C:/Users/Lenovo/Documents/WeChat Files/SworderLau/FileStorage/File/2020-06/'
    filepaths = [path + '6.1 学历.pdf', path + '6.2 学位.pdf']
    savepath = path + '学位学历.pdf'
    pdfMerge(filepaths, savepath)
if __name__ == '__main__':
    main()
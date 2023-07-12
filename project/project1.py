# generate pdf >>>
#  multiple pdf to single Pdf file change :::::

from PyPDF2 import PdfMerger
AllPdf = ['FRONTENresume.pdf', "ResumeMERN.pdf"]

ourMerger = PdfMerger()

for newPdf in AllPdf:
    ourMerger.append(newPdf)

ourMerger.write('doubleResume.pdf')
ourMerger.close()

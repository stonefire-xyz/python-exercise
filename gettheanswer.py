import PyPDF2
fileopen = open('/home/killer/Documents/pythonlite.pdf','rb')
fileread = PyPDF2.PdfFileReader(fileopen)
pdfwrite = PyPDF2.PdfFileWriter()
filetowrite = open('/home/killer/Documents/pythonanswer.pdf','wb')
for i in range(397,408):
    thecontent = fileread.getPage(i)
    pdfwrite.addPage(thecontent)
pdfwrite.write(filetowrite)
fileopen.close()
filetowrite.close()

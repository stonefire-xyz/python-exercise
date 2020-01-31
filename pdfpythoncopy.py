import PyPDF2
def pdf20pagecheckout(m):
    pdffile = open('/home/killer/Documents/Learningvi&&vim.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdffile)
    pdfwriter = PyPDF2.PdfFileWriter()

    for i in range(m,m+20):
        pageobj = pdfReader.getPage(i)
        pdfwriter.addPage(pageobj)

    pdfOutputFile = open('/home/killer/document/learningvim'+str(m)+'.pdf','wb')
    pdfwriter.write(pdfOutputFile)
    pdffile.close()
    pdfOutputFile.close()

m=0
for i in range(20):
    pdf20pagecheckout(m)
    m=m+20 

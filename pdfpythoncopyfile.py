import PyPDF2
def pdf20pagecheckout(m,f):
    pdffile = open('/home/killer/Documents/'+str(f)+'.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdffile)
    pdfwriter = PyPDF2.PdfFileWriter()

    for i in range(m,m+20):
        pageobj = pdfReader.getPage(i)
        pdfwriter.addPage(pageobj)

    pdfOutputFile = open('/home/killer/document/'+str(f)+''+str(m)+'.pdf','wb')
    pdfwriter.write(pdfOutputFile)
    pdffile.close()
    pdfOutputFile.close()

m=0
f='unixshell'
for i in range(20):
    pdf20pagecheckout(m,f)
    m=m+20 

import PyPDF2
import re

# open the pdf file
# myfile = open('ogloszenie_12215.pdf', mode='rb')
pdf_reader = PyPDF2.PdfFileReader('ogloszenie_12215.pdf')
# myfile.close()
# get number of pages
NumPages = pdf_reader.getNumPages()

# define keyterms
String = "Niezależna praca od Systemu CAD (brak konieczności instalacji sytemu CAD jako bazy dla CAM)"

page = pdf_reader.getPage(8)
extracted_page = page.extractText()
ResSearch = re.search(String, extracted_page)
print(ResSearch)

# extract text and do the search
# for i in range(0, NumPages):
#     PageObj = pdf_reader.getPage(i)
#     print("this is page " + str(i))
#     Text = PageObj.extractText()
#     # print(Text)
#     ResSearch = re.search(String, Text)
#     print(ResSearch)
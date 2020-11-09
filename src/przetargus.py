import PyPDF2
import re

from pdfminer import high_level

local_pdf_filename = "ogloszenie_12215.pdf"
pages = [7] # just the first page

extracted_text = high_level.extract_text(local_pdf_filename, "", pages)
extracted_text_low = extracted_text.lower()
extracted_text_clean = re.sub('[^\s\d\w]', '', extracted_text.lower()) #czyszczenie Sringa
print(extracted_text_clean)


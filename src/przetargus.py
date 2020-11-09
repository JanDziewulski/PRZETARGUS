#Pckg install
import PyPDF2
import re
from pdfminer import high_level

def text_recon(text):
    """Loading and cleaning pdf file"""
    local_pdf_filename = "ogloszenie_12215.pdf" #path to file
    pages = [7] #page number

    extracted_text = high_level.extract_text(local_pdf_filename, "", pages)
    extracted_text_low = extracted_text.lower()
    extracted_text_clean = re.sub('[^\s\d\w]', '', extracted_text.lower()) #text clean
    # print(extracted_text_clean)

    """Reading and converting searched text"""
    # reg_rext = "niezależna praca od systemu cad (brak konieczności instalacji sytemu cad jako bazy dla cam)"
    reg_rext_cln = re.sub('[^\s\d\w]', '', 'niezależna praca od systemu cad (brak konieczności instalacji sytemu cad jako bazy dla cam)') #cleaned text
    text_to_list = list(reg_rext_cln)

    """List with item paris"""
    if len(text_to_list) % 2 == 0:
        pair_list = [text_to_list[i] + ' ' + text_to_list[i+1] for i in range(0, len(text_to_list), 2)]
    else:
        pair_list = [text_to_list[i] + ' ' + text_to_list[i+1] for i in range(0, len(text_to_list)-1, 2)]

    count = 0
    for i in range(len(pair_list)):
        founded_item = re.search(pair_list[i], extracted_text_clean)
        if founded_item.group() == pair_list[i]:
            count += 1

    c_ratio = count/len(pair_list)
    if c_ratio == 1:
        print('Pełen sukces kurwo')
    elif 1 > c_ratio >= 0.7:
        print('Sprawdź jeszcze ręcznie ')
    else:
        print('Padaka')


if __name__ == '__main__':
    from openpyxl import load_workbook
    workbook = load_workbook(filename="Wymagania przetargowe.xlsx")
    sheet = workbook.active



    for value in sheet.iter_rows(min_row=2, max_row=4, min_col=2 ,max_col= 4,values_only=True):
        text_recon(value)


# print(item_counter(s))



# print(text_to_list)

# li = list(string.split(" "))
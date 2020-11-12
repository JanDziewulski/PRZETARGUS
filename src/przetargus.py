# Pckg install

import re
from pdfminer import high_level
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
import io
import os
import time
from openpyxl import load_workbook
# import frontend as fr


# find_email_from_pdf = r'(\w+([@])\w+.\w+)|(\w+.\w+([@])\w+.\w+)'
#find_nip_fpdf = r'NIP(\W+\d{10})|NIP(\W+PL\d{10})|NIP(\W+PL\d{3}-\d{2,3}-\d{2}-\d{2,3})|NIP(\W+\d{3}-\d{2,3}-\d{2}-\d{2,3})'

def pdf_info(file):
    fp = open(file, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    print(doc.info)  # The "Info" metadata

def pfd_read(file):
    # pdf_data = fr.browseFiles()
    fp = open(file, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    print(type(retstr))
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    page_no = 0
    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        if pageNumber == page_no:
            interpreter.process_page(page)

            data = retstr.getvalue()

        page_no += 1

    # directory = './przetarg/'
    # filename = time.strftime('przetarg_' + "%Y%m%d-%H%M%S" + '.txt')
    # file_path = os.path.join(directory, filename)
    # if not os.path.isdir(directory):
    #     os.mkdir(directory)
    # file = open(file_path, "wb")
    # file.write(data.encode('utf-8'))
    # file.close()

    return data


def text_recon(text, text_to_recognize):
    """Function that checks the presence of text in a pdf file.

        Args:
            text (str): Parameter imported from .xlsx file.

        Returns:
            bool: The return value. True for success, False otherwise.

        """

    """Loading and cleaning pdf file"""
    # local_pdf_filename = "ogloszenie_12215.pdf"  # path to file
    # pages = [7]  # page number

    # extracted_text = high_level.extract_text(local_pdf_filename, "", pages)
    text = text.lower()
    extracted_text_clean = re.sub('[^\s\d\w]', '', text)  # text clean
    # print(extracted_text_clean)

    """Reading and converting searched text"""
    reg_rext = text_to_recognize
    reg_rext_cln = re.sub('[^\s\d\w]', '', reg_rext)  # cleaned text
    text_to_list = reg_rext_cln.lower().split(' ')
    # print(text_to_list)

    """List with item paris"""
    if len(text_to_list) % 2 == 0:
        pair_list = [text_to_list[i] + ' ' + text_to_list[i + 1] for i in range(0, len(text_to_list), 2)]
    else:
        pair_list = [text_to_list[i] + ' ' + text_to_list[i + 1] for i in range(0, len(text_to_list) - 1, 2)]

    # print(pair_list)

    count = 0
    for i in range(len(pair_list)):
        founded_item = re.search(pair_list[i], extracted_text_clean)
        try:
            if founded_item.group() == pair_list[i]:
                count += 1
        except BaseException:
            pass

            # print('Nie znaleziono tego słowa')

    c_ratio = count / len(pair_list)
    if 1 >= c_ratio >= 0.8:
        return True
        # print('Rozpoznanie z pełnym Sukcesem')
    elif 0.8 > c_ratio >= 0.5:
        print('Sprawdź jeszcze ręcznie ')
        return False
    else:
        return False
        print('Współczynnik rozpoznania {}'.format(round(c_ratio, 2)))

def text_from_excel():

    """
    emp_list[0][0] - opis funkcjonalności, np. Wbudowana baza uchwytów, imadła, uchwyty 3 szczękowe, łapy dociskowe (niedopuszczalne jest dostarczenie bazy osobno poza systemem),
    emp_list[0][1] - nazwa programu, np. Edgecam
    emp_list[0][2] - informacje dodatkowe, np. Nie spełniamy wymagań

    :return:
    """
    global iter_num
    workbook = load_workbook(filename="Wymagania przetargowe.xlsx")
    sheet = workbook.active
    iter_num = sheet.max_row
    apn_list = []
    for value in sheet.iter_rows(min_row=2, min_col=2, max_col=4, values_only=True):
        apn_list.append(value)
        # print(value)
        # text_recon(value)
    return apn_list
    # print(apn_list[1][0])




# text_recon()
if __name__ == '__main__':
    # imput_data= pfd_read('ogloszenie_12215.pdf')

    imput_data= pfd_read('ogloszenie_12215.pdf')
    # text_recon(imput_data)
    # print(imput_data)
    # text_from_excel()
    excel_list = text_from_excel()
    for i in range(iter_num - 1):
        val = text_recon(imput_data, excel_list[i][0])
        if val is True:
            print(excel_list[i][1:])
        else:
            print('Nie rozpoznano!')
        # print(excel_list[i][0])




# def defineAList():
#     local_list = ['1','2','3']
#     print "For checking purposes: in defineAList, list is", local_list
#     return local_list
#
# def useTheList(passed_list):
#     print "For checking purposes: in useTheList, list is", passed_list
#
# def main():
#     # returned list is ignored
#     returned_list = defineAList()
#
#     # passed_list inside useTheList is set to what is returned from defineAList
#     useTheList(returned_list)

# main()

# print(item_counter(s))


# print(text_to_list)

# li = list(string.split(" "))

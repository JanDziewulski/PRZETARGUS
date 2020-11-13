from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import time
from przetargus import PDFsearcher
from tkinter import scrolledtext
from statistics import mode
n_object = PDFsearcher()

#Popup with errors
def popupmsg(msg):
    popup = Tk()
    popup.iconbitmap('../ico/favicon.ico')
    popup.resizable(False, False)  # This code helps to disable windows from resizing
    window_height = 100
    window_width = 200
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    popup.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    popup.wm_title("Błąd!")
    label = Label(popup, text=msg)
    label.pack(pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Wybierz plik",
                                          filetypes=(("Plik pdf",
                                                      "*.pdf*"),
                                                     ("all files",
                                                      "*.*")))
    # Change label contents
    label_file_explorer.configure(text="Plik: " + filename, bg='lavender')
    return filename

def clear():
    t1.configure(state='normal')
    t1.delete("1.0","end")
    t2.delete("1.0","end")


def set_text(text):
    t1.configure(state='normal')
    # t1.delete("1.0","end")
    t1.insert(END,f'{text}\n')
    t1.configure(state='disabled')
    return

def set_text2(text):
    t2.configure(state='normal')
    t2.delete("1.0","end")
    t2.insert(END,text)
    t2.configure(state='disabled')
    return

def start():
    my_progress['value'] = 20
    # global text_info
    try:
        text = n_object.pdf_read(filename) # pobieranie warości z nazwy pliku
        my_progress['value'] = 40
        text_info = n_object.pdf_mail_info(text) #pobieranie wartości pdf info z pliku
        text_info_nip = n_object.pdf_nip_info(text)
        print(text_info_nip)
        my_progress['value'] = 50

        adres, name = n_object.niptofront(text_info_nip)
        set_text(text_info) # wprowadzanie wartości do tabelki
        set_text(text_info_nip) # wprowadzanie wartości do tabelki
        set_text(adres)
        set_text(name)
        my_progress['value'] = 75

        excel_list, _ = n_object.text_from_excel()
        _ , iter_num = n_object.text_from_excel()
        program_list = []
        for i in range(iter_num - 1):
            val = n_object.text_recon(text, excel_list[i][0])
            if val is True:
                program_list.append(excel_list[i][1])
                my_progress['value'] = 90
                print(excel_list[i][1:])
            else:
                print('Nie rozpoznano!')
        set_text2(mode(program_list))



    except NameError as e:
        popupmsg(e)
    my_progress['value'] = 100

window = Tk()
window.resizable(False, False)  # This code helps to disable windows from resizing
window_height = 640
window_width = 480

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

blank_space =" "
current_time = time.strftime("%d-%m-%Y-%H:%M")
window.title('PRZETARGUS 1.0.15' + 20* blank_space + 'Data: {}'.format(current_time))
window.iconbitmap('../ico/favicon.ico')

#progressbar
my_progress = ttk.Progressbar(window, orient=HORIZONTAL,
                              length = 300, mode='determinate')
my_progress.place(x=90, y = 500)



label_file_explorer = Label(window,
                            text = "Nie wybrano żadnego pliku *.pdf",
                            width = 40, height = 1, bg="white")


http_link=StringVar()
e1=Entry(window,text='Podaj link', textvariable=http_link,
          bg="white", width=47)
# e1.place(height=40, width=100)
e1.place(x=150, y =105)

button_explore = Button(window,
                        text = "Wybierz plik",
                        command = browseFiles, width = 10)

button_exit = Button(window,
                     text = "Exit",
                     command = exit,
                     width = 10,
                     bg='OrangeRed'
                     )

button_start = Button(window,
                     text = "Start",
                     command = start,
                     width = 10,
                      bg='lavender')

button_clear = Button(window,
                     text = "Wyczyść",
                     command = clear,
                     width = 10,
                      bg='lavender')

# specifying rows and columns
button_explore.place(x =20 ,y = 30)
label_file_explorer.place(x = 150, y= 30)
l1 = Label(window, text = "URL:",width = 10)
l1.place(x = 20, y = 105)

l2 = Label(window, text = "LUB",width = 10)
l2.place(x= 240, y = 70)


button_exit.place(x = 370, y = 600)
button_start.place(x = 275, y = 600)
button_clear.place(x = 20, y = 600)

l2 = Label(window, text = f"Dane\n prospekta:",width = 10, )
l2.place(x= 20, y =200)

# t1 = (window,height= 10, width=35)
# t1=Text(window, height=6, width=35)
# t1.place(x= 150, y = 200)


t1 = scrolledtext.ScrolledText(window, width=35, height=6, wrap=WORD)
t1.place(x= 150, y = 200)


l3 = Label(window, text = f"Przetarg pod:",width = 10)
l3.place(x= 20, y =375)


t2=Text(window, height=2, width=35)
t2.place(x= 150, y = 375)

window.mainloop()
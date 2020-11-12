from tkinter import *
from tkinter import filedialog
import time
# from tkinter import ttk
from przetargus import PDFsearcher

n_object = PDFsearcher()

def popupmsg(msg):
    popup = Tk()
    popup.iconbitmap('../ico/favicon.ico')
    popup.wm_title("!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill=BOTH, pady=10)
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
    label_file_explorer.configure(text="Plik: " + filename, bg='green')

    return filename

def set_text(text):
    t1.configure(state='normal')
    t1.delete("1.0","end")
    t1.insert(END,text)
    t1.configure(state='disabled')
    return

def start():
    # global text_info
    try:
        text = n_object.pdf_read(filename) # pobieranie warości z nazwy pliku
        text_info = n_object.pdf_info(text) #pobieranie wartości pdf info z pliku
        set_text(text_info) # wprowadzanie wartości do tabelki
    except NameError as e:
        popupmsg(e)

window = Tk()

# window.maxsize(450,550)
# window.minsize(450,550)




window.geometry('450x550')

blank_space =" "
current_time = time.strftime("%d-%m-%Y-%H:%M")
window.title('PRZETARGUS 1.0.15' + 20* blank_space + 'Data: {}'.format(current_time))
window.iconbitmap('../ico/favicon.ico')

label_file_explorer = Label(window,
                            text = "Nie wybrano żadnego pliku *.pdf",
                            width = 40, height = 1, bg="white")


http_link=StringVar()
e1=Entry(window,text='Podaj link', textvariable=http_link,
          bg="white", width=50)
# e1.place(height=40, width=100)
e1.grid(column = 2, row = 3, columnspan=1, sticky=W)

button_explore = Button(window,
                        text = "Wybierz plik",
                        command = browseFiles, width = 10)

button_exit = Button(window,
                     text = "Exit",
                     command = exit,
                     width = 10,
                     bg='red'
                     )

button_start = Button(window,
                     text = "Start",
                     command = start,
                     width = 10,
                      bg='green')

# list1=Listbox(window, height=6,width=35)
# list1.grid(row=2,column=0,rowspan=6,columnspan=2)
#
# sb1=Scrollbar(window)
# sb1.grid(row=2,column=2,rowspan=6)
#
# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)
#
# list1.bind('<<ListboxSelect>>',get_info)





# specifying rows and columns

button_explore.grid(column = 1 , row = 1)
label_file_explorer.grid(column = 2, row = 1)
l1 = Label(window, text = "URL:",width = 10)
l1.grid(column = 1 , row = 3)

l2 = Label(window, text = "LUB",width = 10)
l2.grid(column = 3 , row = 2)


button_exit.grid(column = 1, row=5,pady=30, ipady=5, columnspan =2, sticky=W)
button_start.grid(column = 2, row=5,pady=30, ipady=5)

l2 = Label(window, text = f"Info:")
l2.grid(column = 1 , row = 8 )

#
t1 = Text(window,height= 2)
t1.grid(row =6, column =2, columnspan=2)



# button_start.grid(column = 3 , row =20, pady = 450)
# window.grid_columnconfigure(4, minsize=100)


window.mainloop()
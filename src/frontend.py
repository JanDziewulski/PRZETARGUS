from tkinter import *
from tkinter import filedialog
import time
# from tkinter import ttk


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Wybierz plik",
                                          filetypes=(("Plik pdf",
                                                      "*.pdf*"),
                                                     ("all files",
                                                      "*.*")))
    # Change label contents
    label_file_explorer.configure(text="Plik: " + filename)
    return filename

window = Tk()
window.geometry('600x700')
# window.maxsize(600,700)
# window.minsize(600,700)
blank_space =" "
current_time = time.strftime("%d-%m-%Y-%H:%M")
window.title('PRZETARGUS 1.0.15' + 60* blank_space + 'DATA: {}'.format(current_time))
window.iconbitmap('../ico/favicon.ico')

label_file_explorer = Label(window,
                            text = "Nie wybrano żadnego pliku *.pdf",
                            width = 60, height = 1, bg="white")
                            # compound = CENTER)

l1 = Label(window, text = "URL:",width = 10)
l2 = Label(window, text = "LUB",width = 10)

http_link=StringVar()
e1=Entry(window,text='Podaj link', textvariable=http_link,
          bg="white", width = 70)
# e1.place(height=40, width=100)
e1.grid(column = 3, row = 3)

button_explore = Button(window,
                        text = "Wybierz plik",
                        command = browseFiles, width = 10)

button_exit = Button(window,
                     text = "Exit",
                     command = exit,
                     width = 10)



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
label_file_explorer.grid(column = 3, row = 1, pady=10)
l1.grid(column = 2 , row = 3, padx=30)
l2.grid(column = 3 , row = 2, padx=30)
button_explore.grid(column = 2 , row = 1, padx=30)
button_exit.grid(column = 3 , row =20, pady = 150)
window.grid_columnconfigure(4, minsize=100)
window.mainloop()
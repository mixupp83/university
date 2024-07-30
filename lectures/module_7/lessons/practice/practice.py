import tkinter as tk
import os
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберете файл", filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)


window = tk.Tk()
window.title('Проводник')
window.geometry('350x350')
window.configure(bg='black')
window.resizable(False, False)

text = tk.Label(window, text='Файл:', height=5, width=50, background='silver', foreground='blue')
text.grid(column=1, row=1)
button_select = tk.Button(window, height=3, width=20, text='Выбрать файл', background='silver', foreground='blue', command=file_select)
button_select.grid(column=1, row=2, pady=5)

window.mainloop()
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import Frame, Button, Style
import similar
from tkinter import Tk, Frame, BOTH

def search():
    global query
    query = questionText.get()
    print(query)
    kq = similar.format_output(query)
    outputLb.delete('1.0', END)
    if kq == 0:
        outputLb.insert(END, "Không có kết quả phù hợp\n")
    else:
        a = kq
        for i in a:
            for j in i:
                outputLb.insert(END, j)



root = Tk()
root.geometry("800x500+300+100")
root.config(background="#63DDBF")
root.title("Hệ thống tư vấn tuyển sinh tự động")


questionLab = Label(root, text='Hệ thống tư vấn tuyển sinh tự động\n', font=('Arial', 15, 'bold', 'italic'), background="#63DDBF")
questionLab.grid(row=0, column=2)

questionText = StringVar()
el = Entry(root, textvariable=questionText, width=50)
el.grid(row=1, column=2)


quitButton = Button(root, text="TRẢ LỜI", width=12, command=search)

quitButton.grid(row=3, column=2)

outputLb = Text(root, height=18)
outputLb.grid(column=1, columnspan=3, row=4, rowspan=6,  sticky='W')

scrollbar = Scrollbar(root, orient=VERTICAL) # height= not permitted here!
outputLb.config(yscrollcommand=scrollbar.set, font=('Arial', 13, 'bold', 'italic'))
scrollbar.config(command=outputLb.yview)

scrollbar.grid(row=4, column=7, rowspan=6,  sticky='W')

outputLb.insert(END, "")

root.mainloop()
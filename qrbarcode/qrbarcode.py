import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyqrcode
from PIL import Image, ImageTk
import code128
from barcode.writer import ImageWriter


def createwidget():
    text_text = Label(root, text='CODE TEXT', bg='cadetblue4')
    text_text.grid(row=0, column=0, padx=5, pady=5)

    text_entry = Entry(root, width=35, textvariable=qrbarcodeinput)
    text_entry.grid(row=0, column=1, padx =5, pady= 5)

    text_button = Button(root, text='GENERTE', command=generatecode)
    text_button.grid(row=0,  column=2,padx=5, pady=5)

    type_label = Label(root, text='CODE TYPE:', bg='cadetblue4')
    type_label.grid(row=1, column=0, padx = 5, pady= 5)

    radio_qr = Radiobutton(root, text='QR_CODE', variable=radiovariable, value='qrcode')
    radio_qr.grid(row=1, column=1,  pady=1, padx=0 )

    radio_bar = Radiobutton(root, text='barcode', variable=radiovariable, value='barcode')
    radio_bar.grid(row=1, column=2, padx=0, pady=5, )

    code_label = Label(root, text='CODE', bg='cadetblue4')

    root.image_label = Label(root, bg='cadetblue4' )
    root.image_label.grid(row=3, column=1, columnspan= 2, padx=5, pady= 5)


def generatecode():
    codetext = qrbarcodeinput.get()
    radioselection = radiovariable.get()

    if radioselection == 'qrcode':
        if codetext != '':
            codepath = '/home/medusa/Documents/python/scripting'
            codename = codepath + codetext + '.png'
            code_generate = pyqrcode.create(codetext)
            code_generate.png(codename, scale = 10)


            image = Image.open(codename)
            image = image.resize((400, 400), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)

            root.image_label.config(image=image)
            root.image_label.photo = image

        else:
            messagebox.showerror('you need first to enter the text')

    elif radioselection =='barcode':
        if codetext != '':
            barcodepath = '/home/medusa/Documents/python/scripting'
            barcode_name = barcodepath + codetext + '_barcode'
            barcode_generate = code128(codetext, write = ImageWriter())
            barcode_generate.save(barcode_name, writer = ImageWriter())

            image = Image.open(barcode_name)
            image = image.resize((400,400), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)

            root.image_label.config(image = image)
            root.image_label.photo = image

        else:
            messagebox.showerror('plaese enter text first')

root = tk.Tk()
root.title('qrcode and barcode generator')
root.geometry('510x500')
root.config(background='cadetblue4')
qrbarcodeinput = StringVar()
radiovariable = StringVar()
radiovariable.set('qrcode')

createwidget()

root.mainloop()

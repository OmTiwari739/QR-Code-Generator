from tkinter import *
import qrcode

root = Tk()
root.title("QR Code Generator ")
root.geometry("1000x550")
root.config(bg='#55AAFF')
f = ("arial", 50, "bold")
y=5
lab_name = Label(root, text="QR Code Generator", font=f)
root.resizable(False,False)
lab_name.pack(pady=y)

def generate():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("E:\CLG Mini Pooject/"+ str(name)+ ".png")
    global Image
    Image = PhotoImage(file = "E:\CLG Mini Pooject/"+ str(name)+ ".png")
    Image_view.config(image=Image)
    
Image_view = Label(root, bg="#55AAFF")
Image_view.pack(padx=50, pady=10, side=RIGHT)

Label(root, text="Title",fg="white",bg="#55AAFF", font=15).place(x=50,y=170)

title = Entry(root, width=13, font="arial 15")
title.place(x=50, y=200)

entry = Entry(root, width=40, font="arial 15")
entry.place(x=50, y=250)

Button(root, text="Generate", width=20, height=2, bg="white", fg="black", command=generate).place(x=50, y=300)

root.mainloop()
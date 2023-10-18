from tkinter import *
import downloader


def click():
    lbl3 = Label(window, text='Ожидайте...', font=("Arial Bold", 20))
    lbl3.grid(column=50, row=20)
    try:
        search = txt.get().lower()
        downloader.get(search)
        lbl3.destroy()
        lbl2 = Label(window, text='Скачано', font=("Arial Bold", 20))
        lbl2.grid(column=50, row=20)
    except:
        lbl3 = Label(window, text='Ошибка', font=("Arial Bold", 20))
        lbl3.grid(column=50, row=20)


window = Tk()
window.title('Music dowloader')
window.geometry("640x480")

txt = Entry(window, width=50)
txt.grid(column=20, row=40)

lbl = Label(window, text='Введи название песни', font=("Arial Bold", 20))
lbl.grid(column=20, row=30)

btn = Button(window, text="Скачать", font=("Arial Bold", 20), command=click)
btn.configure(width=10, height=5)
btn.grid(column=20, row=60)

window.mainloop()

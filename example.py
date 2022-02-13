from tkinter import *

pencere = Tk()

def sign_in():
    sifre=entry.get()
    if sifre=="yazılım":
        label.config(text="Giriş başarılı")
        entry.destroy()
        buton.destroy()
    else:
        print("yanlış giriş")


label=Label(pencere)
label.config(text="Şifrenizi giriniz",font=("Arial",20))
label.place(x=20,y=20)

entry=Entry(pencere)
entry.place(x=20,y=70)

buton=Button(pencere)
buton.config(text="Giriş yap",bg="black",fg="white",command=sign_in)
buton.place(x=20,y=100)

mainloop()

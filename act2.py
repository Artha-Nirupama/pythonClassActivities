from tkinter import *

window = Tk()
window.title("My First GUI")
window.geometry("500x500")

icon = PhotoImage(file="logo.png")
window.iconphoto(True,icon)
window.config(background="#4287f5")

photo = PhotoImage(file="logo.png")

label = Label(window,text="Wellcome to the Gaming Community!",font=('Arial',40,'bold'),fg='blue',bg='black',relief=RAISED,bd=10,padx=10,pady=10,image=photo,compound='bottom')

label.pack()

window.mainloop()
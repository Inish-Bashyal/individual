from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def login():
    uname=e1.get()
    pwd=e2.get()

    users=["INISH","ADMIN"]

    #applying empty validation
    if uname=='' or pwd=='':
        messagebox.showerror("Error", "All fields required")
    else:
        for i in users:
            if uname==i and pwd=="ADMIN":
                messagebox.showinfo("SUCCESS", "WELCOME")
                login_screen.destroy()
                import mainpage
                break
        j=uname != "INISH" or uname!= "ADMIN"
        if j and pwd != "ADMIN":
            messagebox.showerror("Error", "Wrong username or password!!!")
            e1.delete(0, END)
            e2.delete(0, END)





def loginform():

    global login_screen

    login_screen = Tk()
    login_screen.title("LOG IN")

    canvas=Canvas(login_screen, width=325, height=450)
    image=ImageTk.PhotoImage(Image.open("new login v1.jpg"))
    canvas.create_image(0,0,anchor=NW, image=image)
    canvas.pack()

    login_pic=PhotoImage(file="new login button.png")
    login_screen.maxsize(width=325, height=450)
    login_screen.minsize(width=325, height=450)


    global e1
    global e2


    e1 = StringVar()
    e2 = StringVar()
    message=StringVar()


    loginname = Label(login_screen, text="USERNAME", font=("Sylfaen", 14), fg="white", bg="#531871").place(x=10, y=200)
    e1=Entry(login_screen)
    e1.place(x=120, y=200)


    loginpassword = Label(login_screen, text="PASSWORD", font=("Sylfaen", 14), fg="white", bg="#4d1a76").place(x=10, y=250)
    e2=Entry(login_screen, show="*")
    e2.place(x=120, y=250)


    login_btn=Button(login_screen, image=login_pic, command=login).place(x=95,y=330)



    login_screen.mainloop()

loginform()



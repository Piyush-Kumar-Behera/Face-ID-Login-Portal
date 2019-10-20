from tkinter import *
from Face_Recognition import *
passkeys = {"Saharsh":"Singh","Prakhar":"Pande"}


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x500")
    root.title("Security Authentication")
    root.configure(background = "white")
    label_title = Label(root,font = ("CASTELLAR",20,'bold'),text = "Security Authentication",bg = "white",fg = "red")
    label_title.grid(padx = 28,pady = 50)
    label1 = Label(root,font = ("Times New Roman",15),text = "To proceed for the security verification, Please click the Face Recognition Button below",bg = "white")
    label1.grid(padx = 28,pady = 70)

    def del1():
        root.destroy()

    fr_button = Button(root,font = ("Arial",12),text = "Recognise Face",command = del1)
    fr_button.place(relx = 0.40,rely = 0.8)


    root.mainloop()

    def del2():
        root1.destroy()
        root = Tk()
        root.geometry("800x500")
        root.title("Security Authentication")
        root.configure(background="white")
        label_title = Label(root, font=("CASTELLAR", 20, 'bold'), text="Security Authentication", bg="white", fg="red")
        label_title.grid(padx=28, pady=50)
        label1 = Label(root, font=("Times New Roman", 15),
                       text="To proceed for the security verification, Please click the Face Recognition Button below",
                       bg="white")
        label1.grid(padx=28, pady=70)

        def del1():
            root.destroy()

        fr_button = Button(root, font=("Arial", 12), text="Recognise Face", command=del1)
        fr_button.place(relx=0.40, rely=0.8)

        root.mainloop()
    user_db = ini_user_database()
    FRmodel = load_FRmodel()
    str = do_face_recognition(user_db, FRmodel, 0.6, "saved_image/1.jpg")


    def del5():
        root2.destroy()
    def del4():
        global flag
        p = password.get()
        # print(p)
        # print(type(p))
        # encr = rsa(p)
        # print(encr)
        if p == passkeys[str]:
            # print("yes")
            del5()
            flag = 1
        else:
            del5()
            flag = 0
    if str == "Unknown Person":
        root1 = Tk()
        root1.geometry("800x500")
        root1.title("Security Warning")
        root1.configure(background="white")
        label2_title = Label(root1, font=("CASTELLAR", 30, 'bold'), text="        Security Warning", bg="white", fg="red")
        label2_title.grid(padx=30, pady=50)
        label3 = Label(root1, font=("Times New Roman", 15),text="            User is not registered!!",bg="white")
        label3.grid(padx=28, pady=70)
        fr_button1 = Button(root1, font=("Arial", 12), text="Back", command=del2)
        fr_button1.place(relx=0.40, rely=0.8)
        root1.mainloop()

    else:
        new_str = "Welcome " + str
        root2 = Tk()
        root2.geometry("800x500")

        root2.title("Security Password")
        root2.configure(background="white")

        label4_title = Label(root2, font=("CASTELLAR", 25, 'bold'), text="            Security Password", bg="white", fg="red")
        label4_title.grid(row = 1,padx=40, pady=50)

        label6_title = Label(root2, font=("Arial", 25), text="                 " + new_str + " !! ", bg="white", fg="black")
        label6_title.grid(row = 2)

        label5_title = Label(root2, font=("Arial", 15), text="Password", bg="white", fg="black")
        label5_title.grid(row = 3, padx=20, pady=60)

        flag = 0
        password = StringVar()

        entry1 = Entry(root2,show = '*',textvariable=password)
        entry1.place(relx = .5, rely = 0.51)

        fr_button2 = Button(root2, font=("Arial", 12), text="Submit", command=del4)
        fr_button2.place(relx=0.44, rely=0.65)

        root2.mainloop()
    if flag == 1 :
        root3 = Tk()
        root3.geometry("800x500")
        root3.title("Security Authentication")
        root3.configure(background="white")
        label7_title = Label(root3, font=("CASTELLAR", 20, 'bold'), text="               ACCESS GRANTED!!", bg="white", fg="green")
        label7_title.grid(padx=40, pady=50)
        label8 = Label(root3, font=("Times New Roman", 15),
                       text="                          User is verified.User has been granted complete access",
                       bg="white")
        label8.grid(padx=28, pady=70)
        root3.mainloop()
    else:
        root4 = Tk()
        root4.geometry("800x500")
        root4.title("Security Authentication")
        root4.configure(background="white")
        label9_title = Label(root4, font=("CASTELLAR", 20, 'bold'), text="                ACCESS DENIED!!", bg="white",
                             fg="red")
        label9_title.grid(padx=40, pady=50)
        label10 = Label(root4, font=("Times New Roman", 15),
                       text="                     Incorrect password is submitted.User cannot be granted access",
                       bg="white")
        label10.grid(padx=28, pady=70)
        root4.mainloop()


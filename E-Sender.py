from os import read
from tkinter import *
from tkinter import messagebox

sx = 1050
sy = 500

def rool():
    """
    Label options:
        text = Add the text:
            Text = "the text you want to show"

        bg = Backgrouend Color:
            bg = "color name"

        fg = Foregrouend Color:
            fg = "color name"

        font = Set the font :
            1: font = ("font_name", int(font_size), "bold")
            2: font = "font_name int(font_size) bold"

        padx = x Padding:
            padx = int(X position)

        pady = y Padding:
            pady = int(Y position)

        Relief = border styling = (SUNKEN, RAISED, GROOVE, RIDGE):
            Relief = SUNKEN
            Relief = RAISED
            Relief = GROOVE
            Relief = RIDEG

        borderwidth = border width:
            borderwidth = int(borderwidth)

    Pack options:
        side = pack side position (TOP, BOTTOM, LEFT, RIGHT):
            side = TOP
            side = BOTTOM
            side = LEFT
            side = RIGHT

        Anchor = pack position(nw, ne, se, sw):
            anecor = "nw"
            anecor = "ne"
            anecor = "se"
            anecor = "sw"
        
        fill = fill a object(X, Y):
            fill = X
            fill = Y
        
        padx = X Padding:
            padx = int(X number)

        pady = Y Padding:
            pady = int(Y number)
        """

def Forgot():
    import webbrowser
    webbrowser.open('https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fsxsrf%3DAOaemvKhGfwR0KRhUeeqPYRsNVLg0NY6Ug%3A1632399361297%26q%3Dgmail%2Bforgot%2Bpassword%26spell%3D1%26sa%3DX%26ved%3D2ahUKEwiozr7AiZXzAhWZzDgGHT39ADwQBSgAegQIARAw%26biw%3D1366%26bih%3D661%26dpr%3D1&ec=GAlAAQ&flowName=GlifWebSignIn&flowEntry=AddSession')

def speak(text):
    import pyttsx3
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()  




root = Tk()
root.title(" Send Email -Aditya Banik")
root.wm_iconbitmap("icon.ico")
root.geometry(f"{sx}x{sy}")
    
root.minsize(sx,sy)
root.maxsize(sx,sy)

# lebal
l1 = Label(root,bg= "lightgreen")
# l2 = Label(root,bg= "black")
    
t1 = Label(l1,text="REGISTER EMAIL",bg= "lightgreen",fg="green",font = ("times new roman", 20, "bold"),relief = GROOVE)
        
your_email_text = Label(l1,text="YOUR EMAIL :",bg= "lightgreen",fg="gray",font = ("times new roman", 10, "bold"))
Your_Gmail = StringVar()
your_Email_entry = Entry(l1,width=30,font = ("lucida", 10, "bold"),borderwidth=2,textvariable=Your_Gmail)

your_password_text = Label(l1,text="YOUR PASSWORD :",bg= "lightgreen",fg="gray",font = ("times new roman", 10, "bold"))
Your_Password = StringVar()
your_Password_entry = Entry(l1,width=30,font = ("lucida", 10, "bold"),borderwidth=2,textvariable=Your_Password)

your_name_text = Label(l1,text="YOUR NAME :",bg= "lightgreen",fg="gray",font = ("times new roman", 10, "bold"))
Your_name = StringVar()
your_name_entry = Entry(l1,width=30,font = ("lucida", 10, "bold"),borderwidth=2,textvariable=Your_name)

your_number_text = Label(l1,text="YOUR NUMBER :",bg= "lightgreen",fg="gray",font = ("times new roman", 10, "bold"))
Your_number = StringVar()
your_number_entry = Entry(l1,width=30,font = ("lucida", 10, "bold"),borderwidth=2,textvariable=Your_number)

email_to_text = Label(l1,text="EMAIL TO :",bg= "lightgreen",fg="gray",font = ("times new roman", 10, "bold"))
email_to = StringVar()
email_to_entry = Entry(l1,width=30,font = ("lucida", 10, "bold"),borderwidth=2,textvariable=email_to)

your_subject_text = Label(l1,text="YOUR SUBJECT :",bg= "lightgreen",fg="gray",font = ("times new roman", 10, "bold"))
your_subject = StringVar()
your_subject_entry = Entry(l1,width=30,font = ("lucida", 10, "bold"),borderwidth=2,textvariable=your_subject)

def exit():
    root.destroy()

exit_button = Button(l1,text=" exit  ",font = ("lucida", 10, "bold"),cursor='hand2',command=exit)

def help():
    messagebox.showinfo('Help',"If Need Help Contact To : \nEmail: adityabanik08@gmail.com")

help_button = Button(l1,text="Help",font = ("lucida", 10, "bold"),cursor='hand2', command=help)

forget_button = Button(l1,text="Forget Password",font = ("lucida", 10, "bold"),cursor='hand2',command=Forgot)


email_text = Text(root,width=150,font = ("lucida", 10, "bold"))
scroll = Scrollbar(email_text)

def EmailSend():
    from email.message import EmailMessage
    import smtplib

    

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(Your_Gmail.get(),Your_Password.get())

    email_message = EmailMessage()
    email_message ['From'] = Your_Gmail.get()
    email_message ['To'] = email_to.get()
    email_message ['Subject'] = your_subject.get()
    email_message.set_content(email_text.get(1.0,END))


    server.send_message(email_message)

    messagebox.showinfo("Sent Successfully","Your Email Hasbin Sent Successfully")

def record():
    import datetime
    dat = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M")
    a1 = f"\\------------------------------------{dat}------------------------------------//"
    a2 = f"  Time : {time}"
    a3 = f"  Name : {Your_name.get()}"
    a4 = f"  Number : {Your_number.get()}"
    a5 = f"  Email : {Your_Gmail.get()}"
    a6 = f"  Send To : {email_to.get()}"
    with open('Record.txt','a') as R:
        R.write(f"\n{a1}\n{a2}\n{a3}\n{a4}\n{a5}\n{a6}\n")

def show_mt():
    mm = messagebox.askquestion('Email Send Confirmation',"Are You Sure To Send Email :")
    if mm == 'yes':
        if Your_Gmail.get() == "" or Your_Password.get() == "" or Your_name.get() == "" or Your_number.get() == "" or email_to.get() == "" or your_subject.get() == "" or email_text.get(1.0,END) == "":
            messagebox.showerror("Error","All Fields Are Required")
            
        else:
            try:
                EmailSend()
                record()
            except Exception as e:
                messagebox.showerror("Error",f"{e}")
    else:
        None

    
send_button = Button(l1,text="                              Send                              ",font = ("lucida", 8, "bold"),cursor='hand2',command=show_mt)

def Rec():
    # while True:
        email_text.delete(1.0,END)
        f = open('Record.txt','r')
        email_text.insert(1.0,f.read())
        f.close()
        
        email_text.update()
        


All_Record_button = Button(l1,text="                         All Record                          ",font = ("lucida", 8, "bold"),cursor='hand2',command=Rec)



show_password = IntVar()
show_password_chackbox = Checkbutton(l1,text="Show Password ",bg= "lightgreen",fg="black",onvalue=1,offvalue=0,font = ("times new roman", 10, "bold"),cursor='hand2',variable=show_password)
    
# outher 

# pack
l1.place(x=5,y=5,width=1040,height=175)
# l2.place(x=5,y=185,width=1040,height=310)
t1.place(x=390,y=2)
your_email_text.place(x=50,y=40)
your_Email_entry.place(x=50,y=60)
your_password_text.place(x=50,y=95)
your_Password_entry.place(x=50,y=115)
your_name_text.place(x=300,y=40)
your_name_entry.place(x=300,y=60)
your_number_text.place(x=300,y=95)
your_number_entry.place(x=300,y=115)
email_to_text.place(x=550,y=40)
email_to_entry.place(x=550,y=60)
your_subject_text.place(x=550,y=95)
your_subject_entry.place(x=550,y=115)
exit_button.place(x=800,y=60)
help_button.place(x=855,y=60)
forget_button.place(x=900,y=60)
send_button.place(x=800,y=95)
All_Record_button.place(x=800,y=125)
email_text.place(x=5,y=185,width=1040,height=310)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=email_text.yview)
email_text.config(yscrollcommand=scroll.set)
show_password_chackbox.place(x=50,y=145)
messagebox.showinfo('Turn off Less secure app access',"Go to the Less secure app access section of your Google Account. You might need to sign in.Turn Allow less secure apps off. :")


for i in range(1,900000000000000000000000000000000000000000000):
    if show_password.get() == 1:
        your_Password_entry.update()
        your_Password_entry.config(show="")
        # your_Password_entry.update()
    else:
        your_Password_entry.update()
        your_Password_entry.config(show="=")
        # your_Password_entry.update()

root.mainloop()













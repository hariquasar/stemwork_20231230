from tkinter import *
from tkinter import messagebox
import base64
import os

def encrypt():
    password = code.get()
    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("ENCRYPTION")
        screen2.geometry("400x200")
        screen2.configure(bg="#ed3833")

        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen2,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)
    elif password=="":
        messagebox.showerror("ENCRYPTION","Input Password")
    else:
        messagebox.showerror("ENCRYPTION","Invalid Password")

def decrypt():
    pass

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Encryption")

    Label(text="Enter The Text For Encryption And Decryption",fg="black",font=("Comic Sans MS",12)).place(x=10,y=10)
    text1 = Text(font="Robote 20",bg="white",relief = GROOVE, wrap = WORD, bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter The Passkey For Encryption And Decryption",fg="black",font=("Comic Sans MS",11)).place(x=10,y=170)
    code = StringVar()
    Entry(textvariable = code, width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="ENCRYPT", height="2", width="23",bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT", height="2", width="23",bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)

    screen.mainloop()


main_screen()

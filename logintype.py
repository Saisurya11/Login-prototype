from tkinter import*
from tkinter import messagebox
global loggedusr
loggedusr=''
#import haslib
#win.configure(background="yellow")
def logi():
    global ee1
    global ee2
    ee1=en1.get()
    ee2=en2.get()
    fo=open('users.txt','r')
    userd=list(fo)
    fo.close()
    for i in userd:
        uname,upass=i.strip().split("|")
        if uname == ee1 and upass == ee2:
            logo()
            loggeduser=ee1
            print("success")
            
            return
        
    else:
        messagebox.showerror("error","bad credentials")

def logo():
    canvas.delete('all')
    canvas.config(background="#FFC125")
    Sdd=Label(canvas,text="success",background="#00BFFF",font=("arail",29))
    canvas.create_window(200,50,window=Sdd)
    buy=Button(canvas,text="back to homepage",command=opening)
    canvas.create_window(100,110,window=buy)
    sino=Button(canvas,text="back to sign in",command=signn)
    canvas.create_window(290,110,window=sino)
    deta=Button(canvas,text="show the details",command=showe)
    canvas.create_window(200,170,window=deta)
def showe():
    canvas.delete('all')
    canvas.config(background="blue")
    f=open('users.txt','r')
    df=list(f)
    f.close()
    for i in df:
        uname,upass=i.strip().split('|')
        gh=en1.get()
        if gh == uname:
            loggeduser=uname
            lf=Label(canvas,text=("welcome "+loggeduser),width=20)
            canvas.create_window(150,50,window=lf)
            bh=Button(canvas,text="back",command=signn)
            canvas.create_window(30,30,window=bh)

def signn():
    global en1
    global en2
    global img
    canvas.delete('all')
    canvas.config(background="grey",height=300,width=450)
    canvas.place(x=0,y=0)
    la1=Label(canvas,text="username")
    la2=Label(canvas,text="password")
    canvas.create_window(40,30,window=la1)
    canvas.create_window(40,70,window=la2)

    img=PhotoImage(file="log.png")
    la2=Label(canvas,image=img)
    la2.image=img
    canvas.create_window(300,115,window=la2)
    

    en1=Entry(canvas)
    en2=Entry(canvas,show="*")
    canvas.create_window(135,30,window=en1)
    canvas.create_window(135,70,window=en2)

    bu1=Button(canvas,text="login",command=logi)
    bu2=Button(canvas,text="back",command=opening)
    canvas.create_window(60,120,window=bu1)
    canvas.create_window(130,120,window=bu2)
def val():
    global e1
    global e2
    global canvas
    canvas.delete('all')
    canvas.config(background="lightblue",height=300,width=450)
    canvas.place(x=0,y=0)
    l1=Label(canvas,text="username")
    l2=Label(canvas,text="password")
    e1=Entry(canvas)
    e2=Entry(canvas)
    img=PhotoImage(file="reg.png")
    la1=Label(canvas,image=img)
    la1.image=img
    canvas.create_window(290,95,window=la1)
    canvas.create_window(135,30,window=e1)
    canvas.create_window(135,70,window=e2)
    canvas.create_window(40,30,window=l1)
    canvas.create_window(40,70,window=l2)
    f=Button(canvas,text="register",command=main)
    canvas.create_window(70,150,window=f)
    f1=Button(canvas,text="back",command=opening)
    canvas.create_window(150,150,window=f1)

def main():
    new_username = e1.get()
    new_password = e2.get()

    with open('users.txt', 'r') as file:
        existing_users = [line.strip().split("|")[0] for line in file]
    
    if new_username in existing_users:
        messagebox.showwarning("Existence", "User already exists, Please choose a different username.")
    else:
        with open("users.txt", "a") as file:
            file.write(new_username + "|" + new_password + "\n")
        
        messagebox.showinfo("Success", "Account created successfully")


def opening():
    canvas.delete('all')
    canvas.configure(background="yellow",width=275,height=150)
    canvas.place(x=50,y=40)
    b1=Button(canvas,text="signup",command=val,activebackground="white",activeforeground="black",background="lightblue",foreground="black")
    b2=Button(canvas,text="signin",command=signn,activebackground="white",activeforeground="black",background="lightblue",foreground="black")
    b3=Button(canvas,text="quit",command=win.destroy,activebackground="white",activeforeground="black",background="lightblue",foreground="black")
    canvas.create_window(70,50,window=b1)
    canvas.create_window(210,50,window=b2)
    canvas.create_window(140,100,window=b3)
global win
win=Tk()
win.configure(background="lightblue")
canvas=Canvas(win,background="yellow",width=275,height=150)
canvas.place(x=50,y=40)
win.geometry("380x250+0+0")
win.resizable(0,0)
opening()

win.mainloop()

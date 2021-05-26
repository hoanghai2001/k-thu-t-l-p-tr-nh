from Tkinter import

def On_Click() :
    if(t.get()==True):
        a.title("Welcome!")
    else:
        a.title("Hello!")
def Sk ():
    Ent.configure({"background":"red"})

a = Tk()
a.geometry("500x250")
a.title("Welcome to Tkinter!")

s = stringVar()
s.set("Hello Python!")
lb = Label(a, textvariable = s)

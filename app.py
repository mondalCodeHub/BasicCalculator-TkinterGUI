
from cgitb import text
from shutil import ExecError
from textwrap import fill
from tkinter import *
# funcLogic():
def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == '=':
        if screenValue.get().isdigit():
            value = int(screenValue.get())
        else:
            try:
                value = eval(screenValue.get())
                
            except Exception as e:
                print(e)
                # screenValue.set("Error")
                # screen.update()
                value= "Error"

        screenValue.set(value)
        screen.update()

    elif text =='C':
        screenValue.set("")
        screen.update()
    else :
        screenValue.set(screenValue.get() + text)
        screen.update()
# GUI
root = Tk()
root.title("Basic Calculator - MondalCodeHub")
root.geometry("350x750")
root.minsize(298,745)
root.maxsize(351,755)
root.wm_iconbitmap('icon.ico')
root.config(bg="blue")
# 
# 
# TOP SCREEN VALUE (UserInput)
screenValue = StringVar()
screenValue.set("")
screen = Entry(root, textvar=screenValue, font="lucida 40 bold" , bg='DodgerBlue3', foreground='white')
screen.pack(fill=X, padx=10, pady=10, ipadx=8)

# 9,8,7 -button
framex = Frame(root, bg="blue")
buttonx = Button(framex, text='9',font='lucida 25 bold', padx=10, pady=5 , bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='8',font='lucida 25 bold', padx=10, pady=5 , bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='7',font='lucida 25 bold', padx=10, pady=5 , bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)

framex.pack()
# 
# 6, 5, 4 - Button ()
framex = Frame(root, bg="blue")
buttonx = Button(framex, text='6',font='lucida 25 bold', padx=10, pady=5 , bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='5',font='lucida 25 bold', padx=10, pady=5 , bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='4',font='lucida 25 bold', padx=10, pady=5 , bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)

framex.pack()
# 
# 3,2,1 Button ( )
framex = Frame(root, bg="blue")
buttonx = Button(framex, text='3',font='lucida 25 bold', padx=10, pady=5 , bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5 )
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='2',font='lucida 25 bold', padx=10, pady=5, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='1',font='lucida 25 bold', padx=10, pady=5, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)

framex.pack()
# 
# 0 , - , *
framex = Frame(root, bg="blue")
buttonx = Button(framex, text='0',font='lucida 33 bold', padx=5, pady=1, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='-',font='lucida 33 bold', padx=5, pady=1, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='*',font='lucida 33 bold', padx=5, pady=1, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)

framex.pack()
# 
# / , % , =
framex = Frame(root, bg="blue")
buttonx = Button(framex, text='/',font='lucida 25 bold',  padx=12, pady=1, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='%',font='lucida 20 bold',  padx=10, pady=5, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='=',font='lucida 25 bold',  padx=12, pady=1, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)

framex.pack()

# C< . , 00
framex = Frame(root, bg="blue")
buttonx = Button(framex, text='C',font='lucida 25 bold', padx=8, pady=5, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='.',font='lucida 25 bold', padx=10, pady=5, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)


buttonx = Button(framex, text='+',font='lucida 25 bold', padx=10, pady=5, bg='blue' , foreground='white')
buttonx.pack(side=LEFT , padx=10, pady=5)
buttonx.bind("<Button-1>",click)

framex.pack()
# 
btn2 = Button( text='close', command=quit,bg='red', foreground='white', font='lucida 15 bold').pack()
# 
root.mainloop()

# Created by : Arup Mondal (@mondalCodeHub) 2022
from tkinter import *
bracket_open = True  

def click(event):
    global svalue, bracket_open
    text = event.widget.cget("text")
    print(text)
    
    if text == "=":
        if svalue.get().isdigit():
            value = int(svalue.get())
        else:
            try:
               value = eval(screen.get())  
            except Exception as e:
                print(e)
                svalue.set("Error")  
                return
        svalue.set(value)    

    elif text == 'c':
        svalue.set("")
        screen.update()

    elif text == 'x²':
        try:
            value = float(svalue.get())
            svalue.set(value**2)
        except:
            svalue.set("Error")    

    elif text == '(' or text == ')':
      expr = svalue.get()
      # Add a * before ( if last character is digit or ')'
      if text == '(' and expr and (expr[-1].isdigit() or expr[-1] == ')'):
        svalue.set(expr + '*' + text)
      else:
        svalue.set(expr + text)

    elif text == '⌫':
        expr = svalue.get()
        svalue.set(expr[:-1])
        svalue.update()

    else:
        svalue.set(svalue.get() + str(text))
        screen.update()



root =Tk()
root.geometry("400x500")
root.title("Calculator")

#Entry and Value
svalue = StringVar()
svalue.set("")
screen = Entry(root,textvariable=svalue,font ="lucida 20 bold")
screen.pack(fill=X,pady=15)

#Creating Buttons and Frame
f1 = Frame(root,bg='grey')
f1.pack(padx=10)

b1 = Button(f1,text=9,font='Arial 20 bold',padx=10,pady=10)
b1.pack(side=LEFT,padx=10)
b1.bind("<Button-1>",click)

b2 = Button(f1,text=8,font='Arial 20 bold',padx=10,pady=10)
b2.pack(side=LEFT,padx=10)
b2.bind("<Button-1>",click)

b3 = Button(f1,text=7,font='Arial 20 bold',padx=10,pady=10)
b3.pack(side=LEFT,padx=10)
b3.bind("<Button-1>",click)


#More Seperate 3 Buttons
f1= Frame(root,bg='grey')
f1.pack(padx=10)

b4 = Button(f1,text=6,font='Arial 20 bold',padx=10,pady=10)
b4.pack(side=LEFT,padx=10)
b4.bind("<Button-1>",click)

b5 = Button(f1,text=5,font='Arial 20 bold',padx=10,pady=10)
b5.pack(side=LEFT,padx=10)
b5.bind("<Button-1>",click)

b6 = Button(f1,text=4,font='Arial 20 bold',padx=10,pady=10)
b6.pack(side=LEFT,padx=10)
b6.bind("<Button-1>",click)



#More Seperate 3 buttons
f1 = Frame(root,bg='grey')
f1.pack(padx=10)

b7 = Button(f1,text=3,font='Arial 20 bold',padx=10,pady=10)
b7.pack(side=LEFT,padx=10)
b7.bind("<Button-1>",click)

b8 = Button(f1,text=2,font='Arial 20 bold',padx=10,pady=10)
b8.pack(side=LEFT,padx=10)
b8.bind("<Button-1>",click)

b9 = Button(f1,text=1,font='Arial 20 bold',padx=10,pady=10)
b9.pack(side=LEFT,padx=10)
b9.bind("<Button-1>",click)
  


#More seperate 3 buttons

f1 = Frame(root,bg='grey')
f1.pack()

b10 = Button(f1,text=0,font='Arial 20 bold',padx=10,pady=5)
b10.pack(side=LEFT,padx=10)
b10.bind("<Button-1>",click)

b11 = Button(f1,text='-',font='Arial 20 bold',padx=13,pady=5,fg='Green',bg='black')
b11.pack(side=LEFT,padx=10)
b11.bind("<Button-1>",click)

b12= Button(f1,text='+',font='Arial 20 bold',padx=10,pady=5,fg='Green',bg='black')
b12.pack(side=LEFT,padx=10)
b12.bind("<Button-1>",click)



#More seperate 3 buttons
f1 = Frame(root,bg='grey',padx=2)
f1.pack()

b13 = Button(f1,text='*',font='Arial 20 bold',padx=9,pady=5,fg='Green',bg='black')
b13.pack(side=LEFT,padx=10)
b13.bind("<Button-1>",click)

b14 = Button(f1,text='/',font='Arial 20 bold',padx=13,pady=5,fg='Green',bg='black')
b14.pack(side=LEFT,padx=10)
b14.bind("<Button-1>",click)

b = Button(f1,text='x²',font='Arial 20 bold',padx=8,pady=5,fg='Green',bg='black')
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)



#More 3 Buttons
f2 = Frame(root,bg='grey')
f2.pack()

b = Button(f2,text='=',font='Arial 20 bold',padx=12,pady=5,fg='Green',bg='black')
b.pack(side=LEFT,padx=10)
b.bind("<Button-1>",click)


b = Button(f2,text=')',font='Arial 20 bold',padx=12,pady=5,fg='Green',bg='black')
b.pack(side=RIGHT,padx=10)
b.bind("<Button-1>",click)

b = Button(f2,text='(',font='Arial 20 bold',padx=13,pady=5,fg='Green',bg='black')
b.pack(side=RIGHT,padx=10)
b.bind("<Button-1>",click)


#Seperately desighned 2 buttons for = and ⌫
b15 = Button(text='c',font='Arial 20 bold',fg='red',bg='black')
b15.place(x=360,y=90)
b15.bind("<Button-1>",click)

bb =Button(root,text='⌫',bg='black',fg='green',pady=10,padx=10)
bb.place(x=360, y=60) 
bb.bind("<Button-1>",click)








root.mainloop()
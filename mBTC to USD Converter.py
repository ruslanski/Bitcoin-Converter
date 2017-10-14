from tkinter import *
import os

class BTC(Frame):

    def __init__(self,master):
        self.master=master
        self.buttons()
              
    def buttons(self):
        global e
        e = Entry(root)
        e.pack()
        e.place(x=40,y=10)
        e.focus_set()
        string = e.get()
        try:
            inp=int(string)
        except ValueError:
            pass
    
        convert = Button(root,text='Convert',command=self.calculate,padx=75,pady=3)
        convert.pack()
        convert.place(y=70)


    def calculate(self):

        output=0
        mbtc=5.6273
        amount=50
        inp=0
        l=[]
        amount-=1
        output=float(mbtc)*float(inp)
        Bots=Frame(root)
        Bots.pack(side=BOTTOM)
        del l[:]
        l.append(output)
        #Set attributes of Bottom Logo
        result=Label(Bots,text=round(l[0],3))
        #Place Bottom Logo
        result.grid(row=0,column=0)

root = Tk()
root.title('mBTC to USD Calculator')
root.geometry("200x100+0+0")
app=BTC(root)
root.mainloop()

from tkinter import *
from math import *
def calculate(a):
    try:
        z=eval(a)
        input.set(z)
    except:
        input.set("Input Error!!!")

root=Tk()
root.title("Calculator")
root.geometry("225x250")
root.resizable(1,1)
input=StringVar()
Entry(root,background="linen",font="('arial',20,'bold')",fg="black",textvariable=input).grid(row=0,column=0,columnspan=5,padx=4,pady=4)
Button(root,text="1",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"1"),height=2,width=4,bg="sky blue").grid(row=1,column=0)
Button(root,text="2",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"2"),height=2,width=4,bg="seashell3").grid(row=1,column=1)
Button(root,text="3",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"3"),height=2,width=4,bg="gold").grid(row=1,column=2)
Button(root,text="/",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"/"),height=2,width=4,bg="white").grid(row=1,column=3)
Button(root,text="sq",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"sqrt"),height=2,width=4,bg="tan1").grid(row=1,column=4)
Button(root,text="4",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"4"),height=2,width=4,bg="pink3").grid(row=2,column=0)
Button(root,text="5",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"5"),height=2,width=4,bg="SpringGreen3").grid(row=2,column=1)
Button(root,text="6",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"6"),height=2,width=4,bg="purple1").grid(row=2,column=2)
Button(root,text="*",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"*"),height=2,width=4,bg="salmon1").grid(row=2,column=3)
Button(root,text="Per",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"/100*"),height=2,width=4,bg="slate gray").grid(row=2,column=4)
Button(root,text="7",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"7"),height=2,width=4,bg="gray68").grid(row=3,column=0)
Button(root,text="8",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"8"),height=2,width=4,bg="rosy brown").grid(row=3,column=1)
Button(root,text="9",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"9"),height=2,width=4,bg="snow4").grid(row=3,column=2)
Button(root,text="+",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"+"),height=2,width=4,bg="yellow").grid(row=3,column=3)
Button(root,text="(",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"("),height=2,width=4,bg="coral").grid(row=4,column=4)
Button(root,text=".",fg="black",font="TkFixedFont",command=lambda:input.set("."),height=2,width=4,bg="deep sky blue").grid(row=4,column=2)
Button(root,text="0",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"0"),height=2,width=4,bg="aliceblue").grid(row=4,column=1)
Button(root,text="-",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"-"),height=2,width=4,bg="pink").grid(row=4,column=3)
Button(root,text="=",fg="black",font="TkFixedFont",command=lambda:calculate(input.get()),height=2,width=4,bg="green3").grid(row=5,column=3)
Button(root,text=")",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+")"),height=2,width=4,bg="thistle").grid(row=5,column=4)
Button(root,text="c",fg="black",font="TkFixedFont",command=lambda:input.set(""),height=2,width=4,bg="SeaGreen2").grid(row=5,column=1)
Button(root,text="Fact",fg="black",font="TkFixedFont",command=lambda:input.set("factorial"),height=2,width=4,bg="dodgerblue").grid(row=3,column=4)
Button(root,text="pi",fg="black",font="TkFixedFont",command=lambda:input.set("pi"),height=2,width=4,bg="green").grid(row=4,column=0)
Button(root,text="Exp",fg="black",font="TkFixedFont",command=lambda:input.set("e"),height=2,width=4,bg="pink").grid(row=5,column=2)
Button(root,text="OFF",fg="black",font="TkFixedFont",command=root.quit,height=2,width=4,bg="firebrick1").grid(row=5,column=0)


root.mainloop()



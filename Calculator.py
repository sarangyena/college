from ast import Return
from cgitb import text
from tkinter import *
from tokenize import String
#Global variable
expression=""
#Class
class Bind():
    def __init__(self, master):
        master.bind('=', self.equal)
        master.bind('<Return>', self.equal)
        master.bind('<Escape>', self.close_win)
    #For evaluating the expression
    def func(self, _event=None):
        global expression
        total=str(eval(expression))
        l1.configure(text="Total:" + total)
    #For clearing the entry field   
    def clear(self,_event=None):
        global expression
        expression = ""
        equation.set("")  
    #For adding characters to the global variable and removing excess characters    
    def equal(self,_event=None):
        try:
            global expression
            string=e1.get()
            for x in string:
                if x == '=':
                    continue
                expression = expression + str(x)
            self.func()
            self.clear()
        #Executes when error happens    
        except:
            l1.configure(text="Error")
            self.clear()
    #For closing the GUI with the escape keyboard button
    def close_win(self, _event=None):
        root.destroy()
#For the buttons in the GUI        
def press(num):
    # point out the global expression variable
    global expression
    # concatenation of string
    string1=e1.get()
    expression = string1
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
#For the equal button in the GUI
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        l1.configure(text="Total:" + total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
        equation.set("")
 
    # if error is generate then handle
    # by the except block
    except:
 
        l1.configure(text="Error")
        expression = ""
#For clearing the entry field
def clear():
    global expression
    expression = ""
    equation.set("")
#GUI
root=Tk()
#Class Bind
calc=Bind(root)
#GUI modifications
root.title("Calculator")
root.configure(background='#98989c')
root.geometry('276x423')
equation=StringVar()
#Entry to input numbers
e1=Entry(root,font='Montserrat 15', text='',width=24,bd=2,justify=RIGHT,textvariable=equation, bg='#59595C',fg='#86C4EB')
e1.grid(columnspan=4,row=0,padx=2,pady=2)
#Label to display total
l1=Label(root,font='Montserrat 15', text='', bg='#98989c', fg='#333333')
l1.grid(columnspan=3,row=1)
#Buttons 0-9
but1=Button(root,font='Montserrat 15', text='1',width=5,height=2,command=lambda:press(1), bg='#45454F',fg='#98989C')
but1.grid(column=0,row=2,padx=2)
but2=Button(root,font='Montserrat 15', text='2',width=5,height=2,command=lambda:press(2), bg='#45454F',fg='#98989C')
but2.grid(column=1,row=2,padx=2)
but3=Button(root,font='Montserrat 15', text='3',width=5,height=2,command=lambda:press(3), bg='#45454F',fg='#98989C')
but3.grid(column=2,row=2,padx=2)
but4=Button(root,font='Montserrat 15', text='4',width=5,height=2,command=lambda:press(4), bg='#45454F',fg='#98989C')
but4.grid(column=0,row=3,padx=2)
but5=Button(root,font='Montserrat 15', text='5',width=5,height=2,command=lambda:press(5), bg='#45454F',fg='#98989C')
but5.grid(column=1,row=3,padx=2)
but6=Button(root,font='Montserrat 15', text='6',width=5,height=2,command=lambda:press(6), bg='#45454F',fg='#98989C')
but6.grid(column=2,row=3,padx=2)
but7=Button(root,font='Montserrat 15', text='7',width=5,height=2,command=lambda:press(7), bg='#45454F',fg='#98989C')
but7.grid(column=0,row=4,padx=2)
but8=Button(root,font='Montserrat 15', text='8',width=5,height=2,command=lambda:press(8), bg='#45454F',fg='#98989C')
but8.grid(column=1,row=4,padx=2)
but9=Button(root,font='Montserrat 15', text='9',width=5,height=2,command=lambda:press(9), bg='#45454F',fg='#98989C')
but9.grid(column=2,row=4,padx=2)
but0=Button(root,font='Montserrat 15', text='0',width=5,height=2,command=lambda:press(0), bg='#45454F',fg='#98989C')
but0.grid(column=1,row=5,padx=2)
#Clear Button
clrbut=Button(root,font='Montserrat 15', text='C',width=5,height=2,command=clear, bg='#45454F',fg='#98989C')
clrbut.grid(column=3,row=1,padx=2,pady=2)
#Addition Button
adb=Button(root,font='Montserrat 15', text='+',width=5,height=2,command=lambda:press("+"), bg='#45454F',fg='#98989C')
adb.grid(column=3,row=2,padx=2)
#Substraction Button
mnb=Button(root,font='Montserrat 15', text='-',width=5,height=2,command=lambda:press("-"), bg='#45454F',fg='#98989C')
mnb.grid(column=3,row=3,padx=2)
#Multiplication Button
mpb=Button(root,font='Montserrat 15', text='*',width=5,height=2,command=lambda:press("*"), bg='#45454F',fg='#98989C')
mpb.grid(column=3,row=4,padx=2)
#Division Button
dvb=Button(root,font='Montserrat 15', text='/',width=5,height=2,command=lambda:press("/"), bg='#45454F',fg='#98989C')
dvb.grid(column=3,row=5,padx=2)
#Decimal Button
dcb=Button(root,font='Montserrat 15', text='.',width=5,height=2,command=lambda:press("."), bg='#45454F',fg='#98989C')
dcb.grid(column=0,row=5,padx=2)
#Percentage Button
pcb=Button(root,font='Montserrat 15', text='%',width=5,height=2,command=lambda:press("%"), bg='#45454F',fg='#98989C')
pcb.grid(column=2,row=5,padx=2)
#Equal Button
eqb=Button(root,font='Montserrat 15', text='=',width=24,height=2,command=equalpress, bg='#45454F',fg='#98989C')
eqb.grid(columnspan=4,row=6,padx=2,pady=2)
mainloop()
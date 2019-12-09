
#import tkinter module
from tkinter import *

#create window
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Brett's Python Calculator")
        #screen widget w, h green back and yellow txt
        self.screen = Text(master, state='disabled', width=50, height=5,background="green", foreground="yellow")
        #screen to window
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        self.screen.configure(state='normal')

        #screen value as empty
        self.equation = ''

        #make buttons
        button1 = self.createButton(1)
        button2 = self.createButton(2)
        button3 = self.createButton(3)
        #delete button
        button4 = self.createButton(u"\u232B",None)
        button5 = self.createButton(4)
        button6 = self.createButton(5)
        button7 = self.createButton(6)
        #divison symbol using regex
        button8 = self.createButton(u"\u00F7")
        button9 = self.createButton(7)
        button10 = self.createButton(8)
        button11 = self.createButton(9)
        button12 = self.createButton('*')
        button13 = self.createButton('.')
        button14 = self.createButton(0)
        button15 = self.createButton('+')
        button16 = self.createButton('-')
        # equals with modified parameters 52 width
        button17 = self.createButton('=',None,52)
        #button list
        buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button16,button17]
        count = 0

        #grid manager

        for row in range(1,5):
            for column in range(4):
                buttons[count].grid(row=row,column=column)
                count += 1

        # put =at bottom

        buttons[16].grid(row=5,column=0,columnspan=4)

    def createButton(self,val,write=True,width=7):
            return Button(self.master, text=val,command = lambda: self.click(val,write), width=width)

    def click(self,text,write):
        # makes click function
        # val will be written if true 
        if write == None:

            #make sure there is an equation

            if text == '=' and self.equation:

                # regex divide symbol instead of python

                self.equation= re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                #perform math
                answer = str(eval(self.equation))
                #clear equation
                self.clear_screen()
                #input answer
                self.insert_screen(answer,newline=True)
            elif text == u"\u232B":
                self.clear_screen()
            
            
        else:
            # put text into screen
            self.insert_screen(text)
        

    def clear_screen(self):
        #clear screen
        #delete equation then screen
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value,newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END,value)
        # record screen values
        self.equation += str(value)
        self.screen.configure(state ='disabled')

brett = Tk()
my_gui = Calculator(brett)
brett.mainloop()
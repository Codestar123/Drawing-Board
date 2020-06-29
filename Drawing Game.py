from tkinter import *
import time
class Game:
    def __init__(self):
        #creating the game window
        self.tk = Tk()
        #assigning the name Click to Draw to the tkinter window
        self.tk.title('Click to Draw')
        self.tk.resizable(0,0)
        self.tk.wm_attributes('-topmost',1)
        #setting the colour of the window to black
        self.tk.configure(background = 'black')
        #we create a variabe color which will store the colour to put . we will change it later
        self.color = 'black'
        self.butlist = []
        for x in range(0,18):
            for y in range(0,35):
                self.butlist.append(Button(self.tk,text = '',command = lambda position=x*35+y: self.draw(self.color, position),fg = 'black',bg = 'black',height = 2,width=4))
                if len(self.butlist) != 0 :
                    self.butlist[len(self.butlist) - 1].grid(row = x ,column = y)
                    
                    

        #we create the buttons for choosing the colour and for reseting and erasing
        self.orange = Button(self.tk,text = '',command = lambda : self.colour_choose('orange'),fg = 'black',bg = 'orange',height = 2,width=4)
        self.orange.grid(column = 0,row = 0)
        self.yellow = Button(self.tk,text = '',command = lambda : self.colour_choose('yellow'),fg = 'black',bg = 'yellow',height = 2,width=4)
        self.yellow.grid(column = 1,row = 0)
        self.green = Button(self.tk,text = '',command = lambda : self.colour_choose('light green'),fg = 'black',bg = 'light green',height = 2,width=4)
        self.green.grid(column = 2,row = 0)
        self.red = Button(self.tk,text = '',command = lambda : self.colour_choose('red'),fg = 'black',bg = 'red',height = 2,width=4)
        self.red.grid(column = 3,row = 0)
        self.brown = Button(self.tk,text = '',command = lambda : self.colour_choose('brown'),fg = 'black',bg = 'brown',height = 2,width=4)
        self.brown.grid(column = 1,row = 1)
        self.blue = Button(self.tk,text = '',command = lambda : self.colour_choose('blue'),fg = 'black',bg = 'blue',height = 2,width=4)
        self.blue.grid(column = 2,row = 1)
        self.reset_but = Button(self.tk,text = 'Reset',command =self.reset,height = 2,width=4, fg = 'white',bg = 'black')
        self.reset_but.grid(column = 3,row = 1)
        self.erase = Button(self.tk,text = 'Eraser',command = lambda : self.colour_choose('black'),fg = 'white',bg = 'black',height = 2,width=4)
        self.erase.grid(column = 0,row = 1)
        
                
    def colour_choose(self,colour):
        #this function will put the colour in the variable
        self.color = colour
    def draw(self,colour,position):
        self.butlist[position]['bg'] = colour
        
    def reset(self):
        self.tk.destroy()
        self.__init__()
        
g = Game()
g.tk.mainloop()

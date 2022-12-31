#A message along with coordinates
from breezypythongui import EasyFrame

class BasicWindow2(EasyFrame):
    #To display quadrants in a window

    def __init__(self, title="Hello!", width=100, height=100, background="yellow", resizable=True):
        super().__init__(title, width, height, background, resizable)
        #Sets up the window and the labels 
        self.addLabel(text="(0,0)", row=0, column=0, sticky="NSEW")
        self.addLabel(text="(0,1)", row=0, column=1, sticky="NSEW")
        self.addLabel(text="(All The best!)", row=1, column=0, sticky="NSEW", columnspan=2)
        #The sticky attribute as a keyword argument specifies the grid position 
        #If sticky is not used, the default argument is northwest. (aligned to the left side of the window)
        #columnspan tells the layout manager that you wish for this widget to occupy more than 1 column, i.e. spans across 2 columns
        #columnspan=2, means it spans it soans across columns 1 and 2
        #same holds true for rowspan also

def main():
    BasicWindow2().mainloop()

if __name__ == "__main__":
    main()

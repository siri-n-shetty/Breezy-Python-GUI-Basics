#shows coordinates
from breezypythongui import EasyFrame

class BasicWindow(EasyFrame):
    #To display quadrants in a window

    def __init__(self, title="Hello!", width=100, height=100, background="yellow", resizable=True):
        super().__init__(title, width, height, background, resizable)
        #Sets up the window and the labels 
        self.addLabel(text="(0,0)", row=0, column=0, sticky="NSEW")
        self.addLabel(text="(0,1)", row=0, column=1, sticky="NSEW")
        self.addLabel(text="(1,0)", row=1, column=0, sticky="NSEW")
        self.addLabel(text="(1,1)", row=1, column=1, sticky="NSEW")
        #The sticky attribute is a keyword argument which specifies the grid position 
        #If sticky is not used, the default argument is northwest. (aligned to the left side of the window)

def main():
    BasicWindow().mainloop()

if __name__ == "__main__":
    main()

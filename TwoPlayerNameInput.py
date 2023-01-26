from breezypythongui import EasyFrame

class MyFrame(EasyFrame):
    def __init__(self):
        super().__init__("My Frame")
        # Create a turtle canvas
        self.canvas = self.addCanvas(row=0, column=0, columnspan=2)
        # Create and display the login page
        self.login_page = self.LoginPage(self)
        self.login_page.grid(row=0, column=0)        

    class LoginPage(EasyFrame):
        def __init__(self, parent):
            super().__init__(parent)
            self.parent = parent
            # Add GUI components and logic for the login form
            self.addLabel("Username of Player 1:", row=0, column=0)
            self.usernameField1 = self.addTextField(text="", row=0, column=1)

            self.addLabel("Username of Player 2:", row=1, column=0)
            self.usernameField2 = self.addTextField(text="", row=1, column=1)

            self.submit_button = self.addButton(text="Submit", row=2, column=0, command=self.login)

        def login(self):
            global username1
            global username2
            # Validate the user input and authenticate the user
            username1 = self.usernameField1.getText()
            username2 = self.usernameField2.getText()
            if username1 != username2:
                self.parent.play_game()
            else:
                # If the login is unsuccessful, show an error message
                self.addLabel(text="Please enter correct username", row=3, column=0)

    def play_game(self):        
        import sys
        sys.path.append("")
        import connneeect      

def main():
    # Create and display the frame
    frame = MyFrame()
    frame.mainloop()

if __name__ == "__main__":
    main()

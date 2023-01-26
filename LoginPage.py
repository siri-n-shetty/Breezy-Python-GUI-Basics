from breezypythongui import EasyFrame

class LoginPage(EasyFrame):
    def __init__(self):
        super().__init__("Login")
        self.addLabel("Username:", row=0, column=0)
        self.usernameField = self.addTextField(text="", row=0, column=1)

        self.addLabel("Password:", row=1, column=0)
        self.passwordField = self.addTextField(text="",row=1, column=1)
        self.addButton("Login", row=2, column=0, columnspan=2, command=self.login)
    def login(self):
        username = self.usernameField.getText()
        password = self.passwordField.getText()

        # Validate the login information here
        # If the login is successful, close the login page and open the main application window
        # If the login is unsuccessful, display an error message
if __name__ == "__main__":
    LoginPage().mainloop()

def turtlePage():
    screen.turtle()

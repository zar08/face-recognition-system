import tkinter as tk

class LoginRegisterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Login/Register")
        master.geometry("300x150")

        # Create a Login button
        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        # Create a Register button
        self.register_button = tk.Button(master, text="Register", command=self.register)
        self.register_button.pack()

    def login(self):
        # Hide the master window
        self.master.withdraw()

        # Create a new window
        self.login_window = tk.Toplevel(self.master)
        self.login_window.title("Login")
        self.login_window.geometry(self.master.geometry())

        # Create a Label and an Entry for the username
        self.username_label = tk.Label(self.login_window, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.login_window)
        self.username_entry.pack()

        # Create a Label and an Entry for the password
        self.password_label = tk.Label(self.login_window, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.pack()

        # Create a Login button
        self.submit_button = tk.Button(self.login_window, text="submit", command=self.submit)
        self.submit_button.pack(pady=10)

    def register(self):
        # Hide the master window
        self.master.withdraw()

        # Create a new window
        self.register_window = tk.Toplevel(self.master)
        self.register_window.title("Register")
        self.register_window.geometry("250x150")

        # Create a Label and an Entry for the username
        self.username_label = tk.Label(self.register_window, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.register_window)
        self.username_entry.pack()

        # Create a Label and an Entry for the password
        self.password_label = tk.Label(self.register_window, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.register_window, show="*")
        self.password_entry.pack()

        # Create a Label and an Entry for the email
        self.email_label = tk.Label(self.register_window, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.register_window)
        self.email_entry.pack()

        # Create a Register button
        self.register_button = tk.Button(self.register_window, text="Register", command=self.register_submit)
        self.register_button.pack(pady=10)

    def submit(self):
        # Get the username and password from the Entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Print the username and password (for testing purposes)
        print("Username:", username)
        print("Password:", password)

        # Show the master window again
        self.master.deiconify()

        # Destroy the login window
        self.login_window.destroy()

    def register_submit(self):
        # Get the username, password, and email from the Entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        # Print the username, password, and email (for testing purposes)
        print("Username:", username)
        print("Password:", password)
        print("Email:", email)

        # Show the master window again
        self.master.deiconify()

        # Destroy the register window
        self.register_window.destroy()


root = tk.Tk()
my_gui = LoginRegisterGUI(root)
root.mainloop()

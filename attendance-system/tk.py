import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("My App")
        master.geometry("750x500")

        login_button_width = 20
        login_button_height = 2
        self.login_button = tk.Button(master, text="Login", command=self.open_login_window, width=login_button_width, height=login_button_height)
        self.login_button.pack(pady=10)
        self.center_window(self.login_button)

        register_button_width = 20
        register_button_height = 2
        self.register_button = tk.Button(master, text="Register", command=self.open_register_window, width=register_button_width, height=register_button_height)
        self.register_button.pack(pady=10)
        self.center_window(self.register_button)

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (self.master.winfo_width() // 2) - (width // 2)
        y = (self.master.winfo_height() // 2) - (height // 2)
        window.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def open_login_window(self):
        login_window = tk.Toplevel(self.master)
        login_window.title("Login")
        login_window.geometry(self.master.geometry())

        # Add login form elements to login_window here

        back_button = tk.Button(login_window, text="Back", command=login_window.destroy)
        back_button.pack(pady=10)

    def open_register_window(self):
        register_window = tk.Toplevel(self.master)
        register_window.title("Register")
        register_window.geometry(self.master.geometry())

        # Add registration form elements to register_window here

        back_button = tk.Button(register_window, text="Back", command=register_window.destroy)
        back_button.pack(pady=10)

root = tk.Tk()
app = App(root)
print("Program running")
root.mainloop()

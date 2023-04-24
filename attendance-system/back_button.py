import tkinter as tk

def get_button(window, text, color, command, fg='white'):
    button = tk.Button(
                        window,
                        text=text,
                        activebackground="black",
                        activeforeground="white",
                        fg=fg,
                        bg=color,
                        command=command,
                        height=2,
                        width=20,
                        font=('Helvetica bold', 20)
                    )

        self.back_btn_register_window = tk.Button(self.register_window, text='Back', bg='white', command=self.back)
        self.back_btn_register_window.place(relx=0.05, rely=0.95, anchor='sw')
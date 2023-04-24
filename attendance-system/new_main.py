import tkinter as tk
import cv2
from PIL import Image, ImageTk
import os
import face_recognition
import subprocess
import pyttsx3
import windows
from datetime import datetime
import attendance

class App:

    def __init__(self):
        # Main window
        self.main_window = tk.Tk()
        self.main_window.title("Face Recognition System")
        self.main_window.geometry("1200x520+350+100")
        #self.main_window.iconbitmap('resources/frs.ico')

        # Set logo for both windows
        logo = tk.PhotoImage(file='logo/frs.png')
        self.main_window.iconphoto(True, logo)

        # Buttons
        self.login_btn_main_window = windows.get_button(self.main_window, 'Login', 'green', self.login)
        self.login_btn_main_window.place(relx=0.5, rely=0.6, anchor='center')
        self.register_btn_main_window = windows.get_button(self.main_window, 'Register', 'green', self.register)
        self.register_btn_main_window.place(relx=0.5, rely=0.4, anchor='center')

        self.images_path = 'resources'
        self.attendance_path = 'Attendance.csv'

    def dashboard(self):
        # Hide the login window
        self.login_window.withdraw()

        # Create dashboard window
        self.dashboard_window = tk.Toplevel(self.login_window)
        self.dashboard_window.title(self.main_window.title())
        self.dashboard_window.geometry(self.main_window.geometry())

    # Create and place the buttons
        button_names = ["Face Recognition", "Check Camera", "Database", "Add new Face"]
        button_frame = tk.Frame(self.dashboard_window)
        button_frame.pack(pady=20)
        for i in range(len(button_names)):
            if button_names[i] == "Face Recognition":
                command = self.face_recognition
            elif button_names[i] == "Check Camera":
                command = self.check_camera
            elif button_names[i] == "Add new Face":
                command = self.add_new_face
            else:
                command = self.database
            button = tk.Button(button_frame, text=button_names[i], font=("Arial", 12), command=command)
            button.grid(row=0, column=i, padx=20, pady=10)

        # Place the button frame in the center of the window
        button_frame.place(relx=0.5, rely=0.5, anchor="center")

    def face_recognition(self):
        # Hide the dashboard window
        self.dashboard_window.withdraw()

        # Create face recognition window
        self.face_recognition_window = tk.Toplevel(self.dashboard_window)
        self.face_recognition_window.title(self.main_window.title())
        self.face_recognition_window.geometry(self.dashboard_window.geometry())

        # Add back button to register window
        self.back_btn_face_recognition = tk.Button(self.face_recognition_window, text='Back', bg='white', command=self.back_btn_dashboard_face_recog)
        self.back_btn_face_recognition.place(relx=0.05, rely=0.95, anchor='sw')

        self.webcam_label = tk.Label(self.face_recognition_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)
        



    def back_btn_dashboard_face_recog(self):
        self.face_recognition_window.destroy()
        self.dashboard_window.deiconify()

    def add_webcam(self, label):
        self.capture = cv2.VideoCapture(0)

        def update():
            ret, frame = self.capture.read()
            if ret:
                self.most_recent_capture_arr = frame
                self.most_recent_capture_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                self.add_img_to_label(label)
            label.after(15, update)

        update()


    def check_camera(self):
        # Hide the dashboard window
        self.dashboard_window.withdraw()

        # Create check camera window
        self.check_camera_window = tk.Toplevel(self.dashboard_window)
        self.check_camera_window.title(self.main_window.title())
        self.check_camera_window.geometry(self.dashboard_window.geometry())

       # Add back button to check camera window
        self.back_btn_check_camera = tk.Button(self.check_camera_window, text='Back', bg='white', command=self.back_btn_dashboard_check)
        self.back_btn_check_camera.grid(row=1, column=1, padx=10, pady=10, sticky='sw')

        # Label for webcam
        self.webcam_label = windows.get_img_label(self.check_camera_window)
        self.webcam_label.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky='nsew')

        # Add webcam to label
        self.add_webcam(self.webcam_label)


    def back_btn_dashboard_check(self):
        self.check_camera_window.destroy()
        self.dashboard_window.deiconify()

    def add_new_face(self):
        # Hide the dashboard window
        self.dashboard_window.withdraw()

        # Create add new face window
        self.add_new_face_window = tk.Toplevel(self.dashboard_window)
        self.add_new_face_window.title(self.main_window.title())
        self.add_new_face_window.geometry(self.dashboard_window.geometry())

        # Add back button to register window
        self.back_btn_add_new_face = tk.Button(self.add_new_face_window, text='Back', bg='white', command=self.back_btn_dashboard_new_face, width=15)
        self.back_btn_add_new_face.grid(row=0, column=0, padx=10, pady=10, sticky="sw")

        # Add accept and try again buttons
        self.accept_btn_add_new_face = tk.Button(self.add_new_face_window, text='Accept', bg='white', command=self.accept_new_face, width=15)
        self.accept_btn_add_new_face.grid(row=1, column=0, padx=10, pady=10, sticky="sw")

        self.try_again_btn_add_new_face = tk.Button(self.add_new_face_window, text='Try Again', bg='white', command=self.try_again_new_face, width=15)
        self.try_again_btn_add_new_face.grid(row=2, column=0, padx=10, pady=10, sticky="sw")

        # Add name entry and label
        self.name_label = tk.Label(self.add_new_face_window, text='Enter name:', width=15)
        self.name_label.grid(row=3, column=0, padx=10, pady=10, sticky="sw")

        self.name_entry = tk.Entry(self.add_new_face_window, width=30)
        self.name_entry.grid(row=4, column=0, padx=10, pady=10, sticky="sw")

        # Label
        self.webcam_label = windows.get_img_label(self.add_new_face_window)
        self.webcam_label.grid(row=0, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")

        self.add_webcam(self.webcam_label)


    def try_again_new_face(self):
        self.add_new_face_window.destroy()

    def accept_new_face(self):
        self.capture = cv2.VideoCapture(0)
        name = self.name_entry.get().strip()
        if not name:
            tk.messagebox.showerror("Error", "Please enter a name")
            return

        file_path = f"resources/{name}.jpg"
        ret, frame = self.capture.read()
        if ret:
            cv2.imwrite(file_path, frame)
            tk.messagebox.showinfo("Success", f"{name}'s face has been added")
            self.name_entry.delete(0, 'end')
        else:
            tk.messagebox.showerror("Error", "Failed to capture image")
            
            # Show success message
            tk.messagebox.showinfo("Success", f"Image of {name} has been saved.")
        
        # Clear name entry
        self.name_entry.delete(0, tk.END)
        
        # Release webcam
        self.capture.release()
        self.add_new_face_window.destroy()
        self.dashboard_window.deiconify()
    
    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()






    def database(self):
        # Hide the dashboard window
        self.dashboard_window.withdraw()

        # Create add new face window
        self.database_window = tk.Toplevel(self.dashboard_window)
        self.database_window.title(self.main_window.title())
        self.database_window.geometry(self.dashboard_window.geometry())

        # Add back button to register window
        self.back_btn_database = tk.Button(self.database_window, text='Back', bg='white', command=self.back_btn_dashboard)
        self.back_btn_database.place(relx=0.05, rely=0.95, anchor='sw')

    def login(self):
        # Hide the main window
        self.main_window.withdraw()

        # Create the login window
        self.login_window = tk.Toplevel(self.main_window)
        # Inherit main window's title, geometry and icon
        self.login_window.title(self.main_window.title())
        self.login_window.geometry(self.main_window.geometry())

        # Add labels and entries for username and password
        username_label = tk.Label(self.login_window, text='Username:', font=('Arial', 16))
        username_label.place(relx=0.35, rely=0.3, anchor='center')
        password_label = tk.Label(self.login_window, text='Password:', font=('Arial', 16))
        password_label.place(relx=0.35, rely=0.4, anchor='center')
        
       
        button1_event = "<Button-1>"
        fucosout_event = "<FocusOut>"

        # Add the username entry widget
        self.username_entry = tk.Entry(self.login_window, font=('Arial', 16))
        self.username_temp_text = "Enter your username"
        self.username_entry.insert(0, self.username_temp_text)
        self.username_entry.bind(button1_event, self.clear_username_temp_text)
        self.username_entry.bind(fucosout_event, self.restore_username_temp_text)
        self.username_entry.place(relx=0.5, rely=0.3, anchor='center')

        # Add the password entry widget
        self.password_entry = tk.Entry(self.login_window, font=('Arial', 16))
        self.password_temp_text = "Enter your password"
        self.password_entry.insert(0, self.password_temp_text)
        self.password_entry.bind(button1_event, self.clear_password_temp_text)
        self.password_entry.bind(fucosout_event, self.restore_password_temp_text)
        self.password_entry.place(relx=0.5, rely=0.4, anchor='center')

        # Add submit button
        self.submit_btn = tk.Button(self.login_window, text="Submit", command=self.dashboard)
        self.submit_btn.place(relx=0.5, rely=0.5, anchor="center")

        # Add back button to login window
        self.back_btn_login_window = tk.Button(self.login_window, text='Back', bg='white', command=self.back)
        self.back_btn_login_window.place(relx=0.05, rely=0.95, anchor='sw')

    def register(self):
        # Hide the main window
        self.main_window.withdraw()

        # Create the login window
        self.register_window = tk.Toplevel(self.main_window)
        self.register_window.title("Face Recognition System")
        self.register_window.geometry(self.main_window.geometry())
        
        # Add labels and entries for username and password
        username_label = tk.Label(self.register_window, text='Username:', font=('Arial', 16))
        username_label.place(relx=0.35, rely=0.3, anchor='center')
        password_label = tk.Label(self.register_window, text='Password:', font=('Arial', 16))
        password_label.place(relx=0.35, rely=0.4, anchor='center')
        
        button1_event = "<Button-1>"
        fucosout_event = "<FocusOut>"

        # Add the username entry widget
        self.username_entry = tk.Entry(self.register_window, font=('Arial', 16))
        self.username_temp_text = "Enter your username"
        self.username_entry.insert(0, self.username_temp_text)
        self.username_entry.bind(button1_event, self.clear_username_temp_text)
        self.username_entry.bind(fucosout_event, self.restore_username_temp_text)
        self.username_entry.place(relx=0.5, rely=0.3, anchor='center')

        # Add the password entry widget
        self.password_entry = tk.Entry(self.register_window, font=('Arial', 16))
        self.password_temp_text = "Enter your password"
        self.password_entry.insert(0, self.password_temp_text)
        self.password_entry.bind(button1_event, self.clear_password_temp_text)
        self.password_entry.bind(fucosout_event, self.restore_password_temp_text)
        self.password_entry.place(relx=0.5, rely=0.4, anchor='center')

        # Add back button to register window
        self.back_btn_register_window = tk.Button(self.register_window, text='Back', bg='white', command=self.back)
        self.back_btn_register_window.place(relx=0.05, rely=0.95, anchor='sw')

        # Add submit button
        self.submit_btn = tk.Button(self.register_window, text="Submit", command=self.dashboard)
        self.submit_btn.place(relx=0.5, rely=0.5, anchor="center")

    # Temporary text for username and password entries
    def clear_username_temp_text(self, event):
        if self.username_entry.get() == self.username_temp_text:
            self.username_entry.delete(0, "end")

    def restore_username_temp_text(self, event):
        if not self.username_entry.get():
            self.username_entry.insert(0, self.username_temp_text)

    def clear_password_temp_text(self, event):
        if self.password_entry.get() == self.password_temp_text:
            self.password_entry.delete(0, "end")

    def restore_password_temp_text(self, event):
        if not self.password_entry.get():
            self.password_entry.insert(0, self.password_temp_text)
    
    def try_again_new_user(self):
        self.face_recognition_window.destroy()

    def submit(self):
        return
    
    def back(self):
        # Show the master window againZA
        self.main_window.deiconify()

    def back_btn_dashboard_new_face(self):
       
        self.add_new_face_window.destroy()

        self.dashboard_window.deiconify()
    

    def start(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()
    
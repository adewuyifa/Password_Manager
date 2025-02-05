from tkinter import *
from backend import PasswordManagerBE
from tkinter import messagebox

class PasswordManagerGUI:
    def __init__(self, master):
        self.be = PasswordManagerBE()  # Backend instance to handle data
        master.title("Password Manager")
        master.config(padx=50, pady=50)

        # Canvas with resized logo
        self.canvas = Canvas(height=200, width=300)
        self.logo = PhotoImage(file="logo.png").subsample(3, 3)  # Resize the logo
        self.canvas.create_image(150, 100, image=self.logo)  # Center the logo
        self.canvas.grid(row=0, column=1)

        # Labels
        self.website_label = Label(text="Website: ")
        self.website_label.grid(row=1, column=0)
        self.email_label = Label(text="Email: ")
        self.email_label.grid(row=2, column=0)
        self.password_label = Label(text="Password: ")
        self.password_label.grid(row=3, column=0)

        # Input fields
        self.website_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()
        self.website_entry = Entry(width=39, textvariable=self.website_var)
        self.website_entry.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.email_entry = Entry(width=39, textvariable=self.email_var)
        self.email_entry.grid(row=2, column=1, columnspan=3, sticky="NSEW")
        self.password_entry = Entry(width=24, textvariable=self.password_var)
        self.password_entry.grid(row=3, column=1, columnspan=2, sticky="NSEW")

        # Buttons
        self.generate_password_button = Button(text="Generate", command=self.generate_password)
        self.generate_password_button.grid(row=3, column=3, sticky="NSEW")
        self.add_button = Button(text="Add", command=self.save_data)
        self.add_button.grid(row=4, column=1, sticky="NSEW")
        self.clear_button = Button(text="Clear", command=self.clear)
        self.clear_button.grid(row=4, column=2, sticky="NSEW")
        self.search_button = Button(text="Search", command=self.search_password)
        self.search_button.grid(row=4, column=3, sticky="NSEW")

    def generate_password(self):
        """
        Generate a random password using the backend and display it in the password field.
        """
        password = self.be.create_password()
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, password)

    def save_data(self):
        """
        Save the entered website, email, and password to the database.
        Display a success message upon completion.
        """
        if not self.website_var.get() or not self.email_var.get() or not self.password_var.get():
            messagebox.showinfo(title="Warning", message="Please make sure you have not left any field empty!")
        else:
            self.be.save_data(self.website_var.get(), self.email_var.get(), self.password_var.get())
            messagebox.showinfo(title="Success", message="Successfully saved!")
            self.clear()

    def search_password(self):
        """
        Search for a website's credentials in the database.
        If found, populate the email and password fields with the data.
        """
        result = self.be.search_password(self.website_var.get())
        if result is None:
            messagebox.showinfo(title="Not found", message=f"No records found for {self.website_var.get()}")
        else:
            self.email_entry.delete(0, "end")
            self.email_entry.insert(0, result[2])
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, result[3])

    def clear(self):
        """
        Clear all input fields.
        """
        self.email_entry.delete(0, "end")
        self.website_entry.delete(0, "end")
        self.password_entry.delete(0, "end")


def main():
    """
    Initialize the Tkinter GUI and start the main loop.
    """
    main_window = Tk()
    password_manager = PasswordManagerGUI(main_window)
    main_window.mainloop()

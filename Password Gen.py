import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        self.label = tk.Label(master, text="Enter password length:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

    def generate_password(self):
        try:
            length = int(self.entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Please enter a valid length greater than 0.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))

            messagebox.showinfo("Generated Password", password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the length.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import Frame, messagebox

class ActivationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("400x200")

        open_button = tk.Button(self.root, text="Open Activation", command=self.open_activation)
        open_button.pack(pady=50)

    def open_activation(self):
        def activate():
            entered_key = search_entry.get()
            if entered_key == "JPM42-7YTRQ-GF84Y-H2H7D-2G9VM":
                explorer_window.destroy()
                messagebox.showinfo("Activation", "Your Windows Is Activated")
            else:
                messagebox.showerror("Error", "Invalid Activation Key")

        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("Activation Product")
        explorer_window.geometry("600x300")

        tabs = Frame(explorer_window)
        tabs.pack(side="top", fill="x")

        search_label = tk.Label(explorer_window, text="Activate With Windows 10 Activation Key")
        search_label.pack(pady=10)

        search_entry = tk.Entry(explorer_window, width=50)
        search_entry.insert(0, "JPM42-7YTRQ-GF84Y-H2H7D-2G9VM")
        search_entry.pack(pady=5)

        activate_button = tk.Button(explorer_window, text="Activate", command=activate)
        activate_button.pack(pady=10)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ActivationApp(root)
    root.mainloop()
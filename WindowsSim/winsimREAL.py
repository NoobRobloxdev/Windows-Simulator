import tkinter as tk
import tkinter as ttk
from tkinter import messagebox, Text, Frame, Entry, Button
from PIL import Image, ImageTk
import time
import os
import html 

class FakeWindows10:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows 10")
        self.root.geometry("1366x768") 
        self.root.resizable(True,True)

        
        try:
            bg_image = Image.open("desktop_background.png")  
            bg_image = bg_image.resize((1366, 768)) 
            self.bg_image = ImageTk.PhotoImage(bg_image)
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading background image: {e}")
        
        self.taskbar = Frame(self.root, bg="gray", height=40)
        self.taskbar.pack(side="bottom", fill="x")

        
        self.start_button = tk.Button(self.taskbar, text="Start", command=self.toggle_start_menu)
        self.start_button.pack(side="left", padx=1)

       
        self.clock_label = tk.Label(self.taskbar, font=('calibri', 10), bg='gray', fg='white')
        self.clock_label.pack(side="right", padx=10)
        self.update_clock()

      
        self.shutdown_button = tk.Button(self.taskbar, text="CMD", command=self.open_cmd)
        self.shutdown_button.pack(side="right", padx=10)

      
        self.shutdown_button = tk.Button(self.taskbar, text="Under Construction. Do not leak ANYTHING", command=self.open_donotleak)
        self.shutdown_button.pack(side="right", padx=5)
        
        self.shutdown_button = tk.Button(self.taskbar, text="Version 2.0.1  Alpha Update Log", command=self.open_versionlog)
        self.shutdown_button.pack(side="right", padx=5)


        
        self.start_menu = None

        self.create_shortcut("Calculator", 50, 100, self.open_calculator)
        self.create_shortcut("Internet Explorer", 50, 5, self.open_internet_explorer)
        self.create_shortcut("Explorer", 50, 200, self.open_explorer)
        self.create_shortcut("CMD", 50, 300, self.open_cmd)
        self.create_shortcut("Notepad", 50, 400, self.open_notepad)
        self.create_shortcut("Visuali Studio Script", 50, 500, self.open_visual_studio)
        self.create_shortcut("Robloacxi", 50, 600, self.show_fake_robloax)
        self.create_shortcut("MINECRAFT DEV", 220, 5, self.open_minecraft_DEV)
        self.create_shortcut("Activation", 220, 100, self.open_activation)
        self.create_shortcut("Media Player", 220, 200, self.open_mediaplayer)

    def update_clock(self):
       
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def toggle_start_menu(self):
       
        if self.start_menu is None:
            self.start_menu = Frame(self.root, bg='lightgray', width=100, height=300)
            self.start_menu.place(x=0, y=505)

            btn_shutdown = tk.Button(self.start_menu, text="Visuali Studio Script", command=self.open_visual_studio)
            btn_shutdown.pack(fill='both')
            
            btn_shutdown = tk.Button(self.start_menu, text="Shutdown", command=self.shutdown)
            btn_shutdown.pack(fill='both')

            btn_calculator = tk.Button(self.start_menu, text="Calculator", command=self.open_calculator)
            btn_calculator.pack(fill='both')

            btn_internet_explorer = tk.Button(self.start_menu, text="Internet Explorer", command=self.open_internet_explorer)
            btn_internet_explorer.pack(fill='both')

            btn_explorer = tk.Button(self.start_menu, text="Explorer", command=self.open_explorer)
            btn_explorer.pack(fill='both')

            btn_cmd = tk.Button(self.start_menu, text="CMD", command=self.open_cmd)
            btn_cmd.pack(fill='both')

            btn_notepad = tk.Button(self.start_menu, text="Notepad", command=self.open_notepad)
            btn_notepad.pack(fill='both')

            btn_notepad = tk.Button(self.start_menu, text="Microsaroft Store", command=self.open_microsoftstore)
            btn_notepad.pack(fill='both')

            btn_notepad = tk.Button(self.start_menu, text="Roblicx", command=self.show_fake_robloax)
            btn_notepad.pack(fill='both')
        else:
            self.start_menu.place_forget()
            self.start_menu = None





    def open_microsoftstore(self):
        
        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("Microsaroft Store")
        explorer_window.geometry("705x450")

        tabs = Frame(explorer_window)
        tabs.pack(side="top", fill="x")

        button_documents = Button(tabs, text="Robloaci", command=self.show_fake_robloax)
        button_documents.pack(side="left", padx=5)

        button_documents = Button(tabs, text="Visuali Studio Scripts", command=self.open_visual_studio)
        button_documents.pack(side="left", padx=10)
        
        button_documents = Button(tabs, text="Minecraft", command=self.open_minecraft)
        button_documents.pack(side="left", padx=10)

        button_downloads = Button(tabs, text="Win_10_Virus_Script_Fake", command=self.show_fake_website)
        button_downloads.pack(side="left", padx=5)

        explorer_label = tk.Label(explorer_window, text="This is Microsaroft Store", font=("Times New Roman", 14))
        explorer_label.pack(pady=5)
        
        button_downloads = Button(tabs, text="Windows Keys Store", command=self.open_windows_activation)
        button_downloads.pack(side="left", padx=5)
        

    def open_donotleak(self):
        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("DO NOT LEAK. Version 2.0.1.1")
        explorer_window.geometry("750x250")

        tabs = Frame(explorer_window)
        tabs.pack(side="top", fill="x")

        explorer_label = tk.Label(explorer_window, text="Do not Release some photos of this. Do not leak and leak the code. bc you destroying the rulles", font=("Times New Roman", 14))
        explorer_label.pack(pady=20)
        explorer_label = tk.Label(explorer_window, text="This is in ALPHA delevopment. Do not leak it please of this Alpha python script. -LOM_Noob ", font=("Times New Roman", 14))
        explorer_label.pack(pady=20)
        
    def open_versionlog(self):
        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("Version 2.0.1.1 Alpha Update Log")
        explorer_window.geometry("800x350")

        tabs = Frame(explorer_window)
        tabs.pack(side="top", fill="x")

        explorer_label = tk.Label(explorer_window, text="Added Activation ShortCut. In the source code is the key or buy in in Microsoaft store lol", font=("Times New Roman", 14))
        explorer_label.pack(pady=20)
        explorer_label = tk.Label(explorer_window, text="Adding in next update 2.0.2.1 Alpha= New Website Called Hello.crm and new App Called NfCree Antivirus = What will check every thing in the WindowsSim Folder ", font=("Times New Roman", 14))
        explorer_label.pack(pady=20)
    
    def open_mediaplayer(self):
        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("Media Player")
        explorer_window.geometry("800x350")

        tabs = Frame(explorer_window)
        tabs.pack(side="top", fill="x")

        explorer_label = tk.Label(explorer_window, text="Idk how to import 1 songs when there is one song in the Songs Folder in Wim Sim ", font=("Times New Roman", 14))
        explorer_label.pack(pady=20)
        explorer_label = tk.Label(explorer_window, text="Will be added in 2.1.0.1 ", font=("Arial", 24))
        explorer_label.pack(pady=20)


    def shutdown(self):
        
        self.root.quit()

    def create_shortcut(self, name, x, y, command):
       
        button = tk.Button(self.root, text=name, command=command, width=15, height=2)
        button.place(x=x, y=y)

    def open_calculator(self):
       
        calc_window = tk.Toplevel(self.root)
        calc_window.title("Calculator")
        calc_window.geometry("300x400")

        entry = Entry(calc_window, font=("Arial", 24), width=14, borderwidth=2, relief="solid")
        entry.grid(row=0, column=0, columnspan=4)

        def button_click(number):
            current = entry.get()
            entry.delete(0, tk.END)
            entry.insert(tk.END, current + str(number))

        def button_clear():
            entry.delete(0, tk.END)

        def button_equal():
            try:
                result = str(eval(entry.get()))
                entry.delete(0, tk.END)
                entry.insert(tk.END, result)
            except:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")

        buttons = [
            ('7', 1, 1), ('8', 1, 2), ('9', 1, 3),
            ('4', 2, 1), ('5', 2, 2), ('6', 2, 3),
            ('1', 3, 1), ('2', 3, 2), ('3', 3, 3),
            ('0', 4, 1), ('+', 1, 4), ('-', 2, 4),
            ('*', 3, 4), ('/', 4, 4), ('C', 4, 2),
            ('=', 4, 3),
        ]

        for (text, row, col) in buttons:
            if text == "=":
                button = Button(calc_window, text=text, width=10, height=3, command=button_equal)
            elif text == "C":
                button = Button(calc_window, text=text, width=10, height=3, command=button_clear)
            else:
                button = Button(calc_window, text=text, width=10, height=3, command=lambda t=text: button_click(t))
            button.grid(row=row, column=col)

    def open_internet_explorer(self):
       
        ie_window = tk.Toplevel(self.root)
        ie_window.title("Internet Explorer")
        ie_window.geometry("600x800")

        search_label = tk.Label(ie_window, text="Search:")
        search_label.pack(pady=10)

        search_entry = tk.Entry(ie_window, width=50)
        search_entry.pack(pady=5)

        def search_action():
            website = search_entry.get()
            self.show_fake_website(website)

        search_button = tk.Button(ie_window, text="Search", command=search_action)
        search_button.pack(pady=10)

        favorites_button = tk.Button(ie_window, text="Favorites", command=self.show_fake_website)
        favorites_button.pack(pady=10)

        favorites_button = tk.Button(ie_window, text="Google", command=self.show_fake_googlew)
        favorites_button.pack(pady=10)

    def show_fake_website(self, website):
  
        if website == "win10fakepy.crm":
            self.show_fake_image("win10fakepy.png")
        else:
            messagebox.showinfo("Website", f"Welcome to {website}!")
            
    def show_fake_info(self, website):
  
        if website == "Info.crm":
            self.show_fake_image("InfoWinwer.png")
        else:
            self.show_fake_image("InfoWinwer.png")
            

    def show_fake_image(self, image_file):
      
        try:
            image = Image.open(image_file)
            image = image.resize((500, 300))  
            img = ImageTk.PhotoImage(image)
            image_label = tk.Label(self.root, image=img)
            image_label.place(x=300, y=200) 
            image_label.image = img  
        except Exception as e:
            messagebox.showerror("Error", f"Error Loading a Website: {e}")

    def show_fake_googlew(self):
        messagebox.showinfo("Googol", "Googol is Under the construction")

    def show_fake_windowsten(self):
        messagebox.showwarning("Microsaroft", "We are Closed for maitenance")

    def show_fake_robloax(self):
        messagebox.showinfo("Robloacx", "We are Closed for maitenance")
        
    def open_minecraft(self):
        messagebox.showerror("Minecraft", "GONNA BE ADDED IN 2.1.3 Alpha Version ")
    
    
    def open_windows_activation(self):
        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("Activation Keys for Windows Simulator Store")
        explorer_window.geometry("600x300")

        tabs = Frame(explorer_window)
        tabs.pack(side="top", fill="x")

        search_label = tk.Label(explorer_window, text="Buy the Product key for 9 Thousand Dollars or Euros")
        search_label.pack(pady=10)
        
        button_downloads = Button(tabs, text="Buy", command=self.open_windows_pro_activate)
        button_downloads.pack(side="left", padx=5)
        
        
    def open_windows_pro_activate(self):
        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("Windows Product keys")
        explorer_window.geometry("600x600")
        
        search_label = tk.Label(explorer_window, text="Windows Product Keys:")
        search_label.pack(pady=10)
        search_label = tk.Label(explorer_window, text="JPM42-7YTRQ-GF84Y-H2H7D-2G9VM")
        search_label.pack(pady=10)
        search_label = tk.Label(explorer_window, text="JPPHG-W7J68-WXHQ3-G2YCG-2GH3Y")
        search_label.pack(pady=10)
        search_label = tk.Label(explorer_window, text="JPMW4-PV8PB-77YFJ-2VHJY-MKTJ3")
        search_label.pack(pady=10)
        search_label = tk.Label(explorer_window, text="JPVQK-22XR2-JP4MV-CD362-F9PRG")
        search_label.pack(pady=10)
        search_label = tk.Label(explorer_window, text="JPVW6-VQ27V-HT6RF-WFTFF-6JYQ3")
        search_label.pack(pady=10)
        search_label = tk.Label(explorer_window, text="Special Product Keys:")
        search_label.pack(pady=10)
        search_label = tk.Label(explorer_window, text="idkthekeybro")
        search_label.pack(pady=10)
        search_label = tk.Label(explorer_window, text="a")
        search_label.pack(pady=10)

        
    def open_minecraft_DEV(self):
        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("Minecraft DEV")
        explorer_window.geometry("600x600")
        
        tabs = Frame(explorer_window)
        tabs.pack(side="top", fill="x")
        
        button_documents = Button(text="SingerPlayer", command=self.open_minecraft)
        button_documents.pack()
    
    def open_activation(self):
        def activate():
            entered_key = search_entry.get()
            if entered_key == "JPM42-7YTRQ-GF84Y-H2H7D-2G9VM":
                explorer_window.destroy()
                messagebox.showinfo("Activation", "Your Windows Is Activated")
            if entered_key == "JPPHG-W7J68-WXHQ3-G2YCG-2GH3Y":
                explorer_window.destroy()
                messagebox.showinfo("Activation", "Your Windows Is Activated")
            if entered_key == "JPMW4-PV8PB-77YFJ-2VHJY-MKTJ3":
                explorer_window.destroy()
                messagebox.showinfo("Activation", "Your Windows Is Activated")
            if entered_key == "JPVQK-22XR2-JP4MV-CD362-F9PRG":
                explorer_window.destroy()
                messagebox.showinfo("Activation", "Your Windows Is Activated")
            if entered_key == "Idkthekeybro":
                explorer_window.destroy()
                messagebox.showinfo("Activation", "Hey its in the source code in def open_activation.hope this helps")
            if entered_key == "a":
                explorer_window.destroy()
                messagebox.showinfo("Activation", "LOM_Noobs favorite word is a!!!!")
            if entered_key == "JPVW6-VQ27V-HT6RF-WFTFF-6JYQ3":
                explorer_window.destroy()
                messagebox.showinfo("Activation", "Your Windows Is Activated")
            else:
                messagebox.showerror("Error", "Invalid Activation Key")

        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("Activation Windows")
        explorer_window.geometry("600x300")

        tabs = Frame(explorer_window)
        tabs.pack(side="top", fill="x")

        search_label = tk.Label(explorer_window, text="Activate With Windows 10 Activation Key")
        search_label.pack(pady=10)
        
        search_label = tk.Label(explorer_window, text="Buy it in Microsoaft Store")
        search_label.pack(pady=10)

        search_entry = tk.Entry(explorer_window, width=50)
        search_entry.insert(0, "Insert the product key here")
        search_entry.pack(pady=5)

        activate_button = tk.Button(explorer_window, text="Activate", command=activate)
        activate_button.pack(pady=10)    
        
    def open_explorer(self):
        
        explorer_window = tk.Toplevel(self.root)
        explorer_window.title("File Explorer")
        explorer_window.geometry("600x300")

        tabs = Frame(explorer_window)
        tabs.pack(side="top", fill="x")

        button_documents = Button(tabs, text="Documents", command=self.show_documents)
        button_documents.pack(side="left", padx=5)

        button_documents = Button(tabs, text="SECREETS", command=self.show_secrets)
        button_documents.pack(side="right", padx=10)

        button_downloads = Button(tabs, text="Downloads", command=self.show_downloads)
        button_downloads.pack(side="left", padx=5)

        explorer_label = tk.Label(explorer_window, text="This is the Explorer", font=("Times New Roman", 14))
        explorer_label.pack(pady=20)

    def show_documents(self):
       
        messagebox.showinfo("Explorer", "Showing Documents ")

    def show_downloads(self):
       
        messagebox.showinfo("Explorer", "Showing Downloads")

        
    def show_secrets(self):
        messagebox.showinfo("SECRETS!", "Secrets are opened")

    def open_cmd(self):
        
        cmd_window = tk.Toplevel(self.root)
        cmd_window.title("CMD")
        cmd_window.geometry("550x350")

        cmd_entry = tk.Entry(cmd_window, width=90)
        cmd_entry.pack(padx=40, pady=50)

        def execute_command():
            command = cmd_entry.get()
            self.run_cmd(command)

        cmd_button = tk.Button(cmd_window, text="Execute", command=execute_command)
        cmd_button.pack(pady=12)

    def run_cmd(self, command):
       
        if command == "ping":
            messagebox.showinfo("CMD", "ping 1.298.183.1.1")
            messagebox.showerror("CMD", "ping 8.234.892.1.1 has a bug. please fix it in Visual Studio Code")
        if command == "dir":
            messagebox.showinfo("CMD", "C:/Windows/system32")
            messagebox.showerror("CMD", f"C:/Windows/system/SYSTEM.DLL")
        if command == "help":
            messagebox.showinfo("CMD", "CPU: AMD RYZEN 5000 7i, GPU AMD Radeon , RAM: 16GB ")
        if command == "exit":
            self.shutdown()
        if command == "Cleared":
            messagebox.showinfo("CMD", "Cleared - Lilithzplug")
            messagebox.showinfo("CMD", "I'll do it, you lazy bitch")
            messagebox.showinfo("CMD", "Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow,Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow")
            messagebox.showinfo("CMD", "Watch how I walk,Watch how I talk,Watch how I vogue on the floor,Down on the floor")
            messagebox.showinfo("CMD", "Only one can be crowned,Fuck how you feel,As long as I clear the room, the room")
            messagebox.showinfo("CMD", "Ain't nobody clearing nothin',Ain't nobody stealing nothin',Away from me,Away from me")
            messagebox.showerror("CMD", "You can strut across the floor,Let your hair hang down some more,Just for me,Just for me")
            messagebox.showerror("CMD", "These bitches don't support me,These bitches are waiting for my motherfucking downfall, bitch,But I will never motherfucking fall,They're waiting for my downfall, bitch,But I will never fall, bitch,Ten years motherfucking strong in the motherfucking bitch,The only way")
            messagebox.showerror("CMD", "Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow,Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow")
            messagebox.showerror("CMD", "That's what I wanna see (oh-oh-oh),That's what I wanna see (oh-oh-oh),That's what I wanna see (oh-oh-oh)")
            messagebox.showerror("CMD", "That's what I wanna see")
            messagebox.showerror("CMD", "Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow,Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow")
            
        else:
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown commandPORNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown commaFuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow,Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slowFuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow,Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slowFuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow,Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slowFuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow,Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slowFuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow,Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slowFuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slow,Fuck it, let's go (let's go),Take it (take it) real slow,Take it (take it) real slow,Take it (take it) real slownd: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")
            messagebox.showerror("CMD", f"Unknown command: {command}")


    def open_visual_studio(self):
        notepad_window = tk.Toplevel(self.root)
        notepad_window.title("Visuali Studio Script")
        notepad_window.geometry("500x550")

        text_widget = Text(notepad_window)
        text_widget.pack(fill="both", expand=True, padx=5, pady=5)

        save_button = tk.Button(notepad_window, text="Save Python Code", command=lambda: self.save_notepad(text_widget))
        save_button.pack(side="left", padx=10)

        exit_button = tk.Button(notepad_window, text="Exit", command=notepad_window.destroy)
        exit_button.pack(side="right", padx=10)

    def save_notepad(self, text_widget):
       
        text_content = text_widget.get("1.0", tk.END)
        messagebox.showinfo("Visuali Studio Script", "Content saved successfully!")

    def open_notepad(self):
        
        notepad_window = tk.Toplevel(self.root)
        notepad_window.title("Notepad")
        notepad_window.geometry("500x400")

        text_widget = Text(notepad_window)
        text_widget.pack(fill="both", expand=True, padx=5, pady=5)

        save_button = tk.Button(notepad_window, text="Save", command=lambda: self.save_notepad(text_widget))
        save_button.pack(side="left", padx=10)

        exit_button = tk.Button(notepad_window, text="Exit", command=notepad_window.destroy)
        exit_button.pack(side="right", padx=10)

    def save_notepad(self, text_widget):
        
        text_content = text_widget.get("1.0", tk.END)
        messagebox.showinfo("Notepad", "Content saved successfully!")



root = tk.Tk()
fake_windows = FakeWindows10(root)
root.mainloop()

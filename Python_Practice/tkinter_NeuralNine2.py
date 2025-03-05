#Functionality description
#Using these widgets under a class
#for calling function we use (), but for passing as parameter we just write name of function
import tkinter as tk
from tkinter import messagebox
#constructor is going to creat a GUI

class MyGUI():
    def __init__(self):

        self.root =tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        #to add somethings in filemenu
        self.filemenu.add_command(label = "Close", command=self.on_closing) #we can also write exit
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)


        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="My Label", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_stat = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Message", font=('Arial', 16), variable=self.check_stat)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def show_message(self):
        if self.check_stat.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        #print(event.keysym)
        #print(event.state)
        if event.state == 4 and event.keysym == "Return":
            self.show_message()
            #print("Hello!")
        #print(event.keysym)
        #print(event.state)
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you want to quit?"):
        #print("Hello World!")
            self.root.destroy()
        
    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGUI()
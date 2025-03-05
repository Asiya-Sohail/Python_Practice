import tkinter as tk

root = tk.Tk()

root.geometry("600x500")   #dimensions of window
root.title("My First GUI")

#pack or grid or place is for having layout/widgets inside the window

#root is a parent bject of this "label" object
label = tk.Label(root, text="Hello World!", font = ('Microsoft Himalaya', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=2, font=("Microsoft JhengHei", 16))
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Segoe UI Semibold", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("Segoe UI Semibold", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("Segoe UI Semibold", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Segoe UI Semibold", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("Segoe UI Semibold", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("Segoe UI Semibold", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill=tk.X)  #or we can write "x" instead of tk.X

anotherbtn = tk.Button(root, text="TEST")
anotherbtn.place(x=200, y=200,height=200, width=200)

#button = tk.Button(root, text="click", font=("Arial", 10))
#button.pack()

#Entry is used for one line text
#myentry = tk.Entry(root)
#myentry.pack()

root.mainloop()

import tkinter as tk
# from tkinter import filedialog
# from tkinter import ttk

# root = tk.Tk()
# label = tk.Label(root, text="Hello World") #create txt label
# label.pack(padx=20, pady=20)

# root.mainloop()
# q

class HelloWorld(tk.Frame):
    def __init__(self, parent):
        super(HelloWorld, self).__init__(parent)

        self.label = tk.Label(self, text="Hello World")
        self.label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root  =tk.Tk()

    main = HelloWorld(root)
    main.pack(fill="both", expand=True)

    root.mainloop
    
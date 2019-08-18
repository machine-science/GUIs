# from tkinter import *
#
# root = Tk()
#
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# for i in ['Python', 'Ruby', 'Perl', 'C++','HTML','CSS','Marathi','Japanese','Spanish']:
#     chkbox = Checkbutton(root,text=i)
# chkbox.pack(side=TOP,  fill=X)
#
# chkbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=chkbox.yview)
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# listbox = Listbox(root)
# listbox.pack()
#
# for i in range(100):
#     listbox.insert(END, i)
#
# # attach listbox to scrollbar
# listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)
#
# mainloop()


import tkinter as tk
from tkinter import filedialog

class GUI():
    def __init__(self, button_dict):
        self.root = tk.Tk()
        self.root.title("File Type")

        self.button_dict = button_dict
        row = len(self.button_dict) + 1

        for i,key in enumerate(self.button_dict,1):
            print(i, key)
            self.button_dict[key] = tk.IntVar() # set all values of the dict to intvars
            # set the variable of the checkbutton to the value of our dictionary so that our dictionary is updated each time a button is checked or unchecked
            c = tk.Checkbutton(self.root, text=key, variable=self.button_dict[key])
            c.grid(row=i, sticky=tk.W)

        # include = tk.Button(self.root, text='Include',
        #                     command=self.query_include)
        # include.grid(row=row, sticky=tk.W)

        exclude = tk.Button(self.root, text='Remove',
                            command=self.query_exclude)
        exclude.grid(row=row, sticky=tk.E, padx=10, pady=10)

        quit = tk.Button(self.root, text='Quit', command=self.root.destroy)
        quit.grid(row=row+1, sticky=tk.W)

    def query_include(self):
        for key, value in self.button_dict.items():
            if value.get():
                print(key)

    def query_exclude(self):
        for key, value in self.button_dict.items():
            if not value.get():
                print(key)

    def main(self):
        self.root.mainloop()

if __name__ == "__main__":
    file_dict = {}
    def askFile():
        root = tk.Tk()
        path = filedialog.askopenfilename(title="Select a file")
        root.destroy()
        return path

    path = askFile()
    while path != "":
        file_dict[str(path)]=0
        path = askFile()
    button_dict=file_dict

    print(button_dict)
    gui = GUI(button_dict)
    gui.main()

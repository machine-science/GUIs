import tkinter as tk
from tkinter import *
from tkinter import filedialog


class ScrollableFrame(tk.Frame):
    def __init__(self,root,**kwargs):
        tk.Frame.__init__(self,root,**kwargs)

        # create a vertical scrollbar on canvas
        self.hscrollbar = tk.Scrollbar(self,orient = tk.HORIZONTAL)
        self.vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vscrollbar.pack(side='right',fill='y')
        self.hscrollbar.pack(side="bottom",fill='x')
        # create a canvas
        self.canvas = tk.Canvas(self,bg='#444444', bd=0, height=350, highlightthickness=0,
                                yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar.set)
        self.canvas.pack(side="top",fill="both",expand='true')
        self.vscrollbar.config(command=self.canvas.yview)
        self.hscrollbar.config(command=self.canvas.xview)

        #reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas,**kwargs)
        self.canvas.create_window(0,0,window=self.interior,anchor="nw")

        self.bind("<Configure>", self.set_scrollregion)

    def set_scrollregion(self,event=None):
        '''Set the scroll region on the canvas '''
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

if __name__ == '__main__':
    root = tk.Tk()
    checkbox_pane = ScrollableFrame(root, bg='white')
    checkbox_pane.pack(expand="true", fill="both")
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

    for i,key in enumerate(file_dict,1):
        print(i,key)
        tk.Checkbutton(checkbox_pane.interior,text=str(i)+" "+key).grid(row=i, column=0, sticky='w')

    # btn_checkbox = tk.Button(checkbox_pane.interior, text="Click Me!", command=button_callback)
    # btn_checkbox.grid(row=0, column=0)

    root.mainloop()

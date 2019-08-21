import tkinter as tk
from tkinter import *
from tkinter import filedialog

def doScrolling(file_dict):
    root=tk.Tk()
    root.geometry('500x500')
    root.configure(background='white')
    lbl = Label(root, text="These are the files you have selected",bg="white")
    lbl.pack(side="top",pady=10)
    frm1 = Frame(root,bg="white",width=500, height=500)
    frm = Frame(frm1,bg="white",width=500, height=300)
    

    # create a canvas
    canvas = tk.Canvas(frm,bg='white', bd=0, highlightthickness=0)

    hscrollbar = tk.Scrollbar(frm,orient = tk.HORIZONTAL)
    vscrollbar = tk.Scrollbar(frm, orient=tk.VERTICAL)
    vscrollbar.pack(side='right',fill='y')
    hscrollbar.pack(side="bottom",fill='x')
    canvas.config( yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
    vscrollbar.config(command=canvas.yview)
    hscrollbar.config(command=canvas.xview)
    canvas.pack(side="top",fill="both",expand='true',pady=10)
#     canvas.place(relx=0.5, rely=0.5, relheight=1, relwidth=1)

    #reset the view
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)

    def set_scrollregion(event=None):
        '''Set the scroll region on the canvas '''
        canvas.configure(scrollregion=canvas.bbox('all'))

    interior = tk.Frame(canvas,bg="white",width=500, height=300)
    canvas.create_window(0,0,window=interior,anchor="nw")
    frm.bind("<Configure>", set_scrollregion)
    frm1.pack(side="top",pady=(10,0))
    frm.pack(side="top")
    

    for i,key in enumerate(file_dict,1):
        tk.Checkbutton(interior,text=str(i)+" "+key, bg="white", fg="#009152").grid(row=i+3, column=0, sticky='sw')

    root.mainloop()

#================================================================


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
    
doScrolling(file_dict)
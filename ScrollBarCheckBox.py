import tkinter as tk

class ScrollableFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        # create a canvas object and a vertical scrollbar for scrolling it
        self.vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vscrollbar.pack(side='right', fill="y",  expand="false")
        self.canvas = tk.Canvas(self,
                                bg='#444444', bd=0,
                                height=350,
                                highlightthickness=0,
                                yscrollcommand=self.vscrollbar.set)
        self.canvas.pack(side="left", fill="both", expand="true")
        self.vscrollbar.config(command=self.canvas.yview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas, **kwargs)
        self.canvas.create_window(0, 0, window=self.interior, anchor="nw")

        self.bind('<Configure>', self.set_scrollregion)


    def set_scrollregion(self, event=None):
        """ Set the scroll region on the canvas"""
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


if __name__ == '__main__':
    root = tk.Tk()
    checkbox_pane = ScrollableFrame(root, bg='#444444')
    checkbox_pane.pack(expand="true", fill="both")

    def button_callback():
        for x in range(1,20):
            tk.Checkbutton(checkbox_pane.interior, text="hello world! %s" % x).grid(row=x, column=0)

    btn_checkbox = tk.Button(checkbox_pane.interior, text="Click Me!", command=button_callback)
    btn_checkbox.grid(row=0, column=0)
    root.mainloop()

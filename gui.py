"""
    A simple calculator with basic operations and a menu of options (OOP).

    Author: José De La Cruz
    Created: 2019-08-04
    Modified: 2025-02-25
"""
import tkinter as tk
from tkinter import ttk

IPADX = 6
IPADY = 5
WIDTH = 7


class Gui(tk.Tk):
    """Class that works as the application view"""

    def __init__(self, controller):
        super().__init__()
        self.title('Calculadora')
        self.iconphoto(True, tk.PhotoImage(file='icons/calculadora.png'))
        self.resizable(False, False)
        self.center_window(490, 225)
        self.controller = controller
        self.var_display = tk.StringVar()

        # add menu icons
        self.img_copy = tk.PhotoImage(file='icons/copy.gif')
        self.img_paste = tk.PhotoImage(file='icons/paste.gif')
        self.img_undo = tk.PhotoImage(file='icons/undo.gif')
        self.img_redo = tk.PhotoImage(file='icons/redo.gif')
        self.img_preferences = tk.PhotoImage(file='icons/preferences.gif')
        self.img_exit = tk.PhotoImage(file='icons/exit.gif')
        self.img_help = tk.PhotoImage(file='icons/help.png')
        self.img_about = tk.PhotoImage(file='icons/about.gif')

        # add menu bar
        self.menubar = tk.Menu(self, tearoff=0, relief=tk.FLAT)
        self.configure(menu=self.menubar)

        # add menu file
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Archivo', menu=self.filemenu)
        self.filemenu.add_command(label='Copiar', command=None, accelerator='Ctrl+C', image=self.img_copy, compound=tk.LEFT)
        self.filemenu.add_command(label='Pegar', command=None, accelerator='Ctrl+V', image=self.img_paste, compound=tk.LEFT)
        self.filemenu.add_command(label='Deshacer', command=None, accelerator='Ctrl+Z', image=self.img_undo, compound=tk.LEFT)
        self.filemenu.add_command(label='Rehacer', command=None, accelerator='Ctrl+Y', image=self.img_redo, compound=tk.LEFT)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Preferencias', command=None, image=self.img_preferences, compound=tk.LEFT)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Salir', command=self.quit, accelerator='Ctrl+Q', image=self.img_exit, compound=tk.LEFT)

        # add menu help
        self.ayudamenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Ayuda', menu=self.ayudamenu)
        self.ayudamenu.add_command(label='Ayuda', command=None, image=self.img_help, accelerator='F1', compound=tk.LEFT)
        self.ayudamenu.add_command(label='Acerca de', command=None, image=self.img_about, compound=tk.LEFT)

        # display frame
        self.frm_display = ttk.Frame(self)
        self.frm_display.grid(row=1, column=0, padx=5, pady=5)

        # row 0: display
        self.ety_display = ttk.Entry(self.frm_display, textvariable=self.var_display, width=31, justify=tk.RIGHT, font=('Consola', 16, 'bold'))
        self.ety_display.grid(row=1, column=0, columnspan=4, ipady=10)

        # buttons frame
        self.frm_buttons = ttk.Frame(self)
        self.frm_buttons.grid(row=2, column=0, padx=5, pady=5)

        # buttons style
        self.btn_style = ttk.Style()
        self.btn_style.configure('TButton', background='white')

        # row 1
        self.btn_seven = ttk.Button(self.frm_buttons, text='7', width=WIDTH, command=lambda: self.controller.on_click_button('7'))
        self.btn_seven.grid(row=2, column=0, ipadx=IPADX, ipady=IPADY)
        self.btn_eight = ttk.Button(self.frm_buttons, text='8', width=WIDTH, command=lambda: self.controller.on_click_button('8'))
        self.btn_eight.grid(row=2, column=1, ipadx=IPADX, ipady=IPADY)
        self.btn_nine = ttk.Button(self.frm_buttons, text='9', width=WIDTH, command=lambda: self.controller.on_click_button('9'))
        self.btn_nine.grid(row=2, column=2, ipadx=IPADX, ipady=IPADY)
        self.btn_div = ttk.Button(self.frm_buttons, text='÷', width=WIDTH, command=lambda: self.controller.on_click_button('÷'))
        self.btn_div.grid(row=2, column=3, ipadx=IPADX, ipady=IPADY)
        self.btn_undo = ttk.Button(self.frm_buttons, text='Deshacer', width=WIDTH, command=lambda: self.controller.on_click_function('Deshacer'))
        self.btn_undo.grid(row=2, column=4, ipadx=IPADX, ipady=IPADY)
        self.btn_clear = ttk.Button(self.frm_buttons, text='Limpiar', width=WIDTH, command=lambda: self.controller.on_click_function('Limpiar'))
        self.btn_clear.grid(row=2, column=5, ipadx=IPADX, ipady=IPADY)

        # row 2
        self.btn_four = ttk.Button(self.frm_buttons, text='4', width=WIDTH, command=lambda: self.controller.on_click_button('4'))
        self.btn_four.grid(row=3, column=0, ipadx=IPADX, ipady=IPADY)
        self.btn_five = ttk.Button(self.frm_buttons, text='5', width=WIDTH, command=lambda: self.controller.on_click_button('5'))
        self.btn_five.grid(row=3, column=1, ipadx=IPADX, ipady=IPADY)
        self.btn_six = ttk.Button(self.frm_buttons, text='6', width=WIDTH, command=lambda: self.controller.on_click_button('6'))
        self.btn_six.grid(row=3, column=2, ipadx=IPADX, ipady=IPADY)
        self.btn_mul = ttk.Button(self.frm_buttons, text='x', width=WIDTH, command=lambda: self.controller.on_click_button('x'))
        self.btn_mul.grid(row=3, column=3, ipadx=IPADX, ipady=IPADY)
        self.btn_rig_par = ttk.Button(self.frm_buttons, text='(', width=WIDTH, command=lambda: self.controller.on_click_button('('))
        self.btn_rig_par.grid(row=3, column=4, ipadx=IPADX, ipady=IPADY)
        self.btn_left_par = ttk.Button(self.frm_buttons, text=')', width=WIDTH, command=lambda: self.controller.on_click_button(')'))
        self.btn_left_par.grid(row=3, column=5, ipadx=IPADX, ipady=IPADY)

        # row 3
        self.btn_one = ttk.Button(self.frm_buttons, text='1', width=WIDTH, command=lambda: self.controller.on_click_button('1'))
        self.btn_one.grid(row=4, column=0, ipadx=IPADX, ipady=IPADY)
        self.btn_two = ttk.Button(self.frm_buttons, text='2', width=WIDTH, command=lambda: self.controller.on_click_button('2'))
        self.btn_two.grid(row=4, column=1, ipadx=IPADX, ipady=IPADY)
        self.btn_three = ttk.Button(self.frm_buttons, text='3', width=WIDTH, command=lambda: self.controller.on_click_button('3'))
        self.btn_three.grid(row=4, column=2, ipadx=IPADX, ipady=IPADY)
        self.btn_sub = ttk.Button(self.frm_buttons, text='-', width=WIDTH, command=lambda: self.controller.on_click_button('-'))
        self.btn_sub.grid(row=4, column=3, ipadx=IPADX, ipady=IPADY)
        self.btn_square = ttk.Button(self.frm_buttons, text='x²', width=WIDTH, command=lambda: self.controller.on_click_button('\u00b2'))
        self.btn_square.grid(row=4, column=4, ipadx=IPADX, ipady=IPADY)
        #self.btn_square_root = ttk.Button(self.frm_buttons, text='√', width=WIDTH, command=lambda:self.controller.on_click_button('√'))
        self.btn_square_root = ttk.Button(self.frm_buttons, text='√', width=WIDTH, command=lambda: self.controller.on_click_button('\u00bd'))
        self.btn_square_root.grid(row=4, column=5, ipadx=IPADX, ipady=IPADY)

        # row 4
        self.btn_zero = ttk.Button(self.frm_buttons, text='0', width=WIDTH, command=lambda: self.controller.on_click_button('0'))
        self.btn_zero.grid(row=5, column=0, ipadx=IPADX, ipady=IPADY)
        self.btn_dot = ttk.Button(self.frm_buttons, text=',', width=WIDTH, command=lambda: self.controller.on_click_button(','))
        self.btn_dot.grid(row=5, column=1, ipadx=IPADX, ipady=IPADY)
        self.btn_per = ttk.Button(self.frm_buttons, text='%', width=WIDTH, command=lambda: self.controller.on_click_button('%'))
        self.btn_per.grid(row=5, column=2, ipadx=IPADX, ipady=IPADY)
        self.btn_add = ttk.Button(self.frm_buttons, text='+', width=WIDTH, command=lambda: self.controller.on_click_button('+'))
        self.btn_add.grid(row=5, column=3, ipadx=IPADX, ipady=IPADY)
        self.btn_equals = ttk.Button(self.frm_buttons, text='=', width=18, command=lambda: self.controller.on_click_function('='))
        self.btn_equals.grid(row=5, column=4, columnspan=2, ipadx=IPADX, ipady=IPADY)


    def center_window(self, w, h):
        """Center window"""
        x = (self.winfo_screenwidth() - w) / 2
        y = (self.winfo_screenheight() - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def start_mainloop(self):
        """Run the main window loop"""
        self.mainloop()

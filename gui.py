import tkinter as tk
from tkinter import ttk
from about import About

IPADX = 6
IPADY = 5
WIDTH = 7


class Gui(tk.Tk):
    """ Class that works as the application view """
    def __init__(self, controller):
        super().__init__()
        self.title('Calculator')
        self.iconphoto(True, tk.PhotoImage(file='asset/images/calculator.png'))
        self.resizable(False, False)
        self.center_window(331, 401)
        self.controller = controller
        # creaate instance
        self.var_display = tk.StringVar()

        # create menu icons
        self.img_copy = tk.PhotoImage(file='asset/images/copy.gif')
        self.img_paste = tk.PhotoImage(file='asset/images/paste.gif')
        self.img_undo = tk.PhotoImage(file='asset/images/undo.gif')
        self.img_redo = tk.PhotoImage(file='asset/images/redo.gif')
        self.img_preferences = tk.PhotoImage(file='asset/images/preferences.gif')
        self.img_exit = tk.PhotoImage(file='asset/images/exit.gif')
        self.img_help = tk.PhotoImage(file='asset/images/help.png')
        self.img_about = tk.PhotoImage(file='asset/images/about.gif')

        # create menu bar
        self.menubar = tk.Menu(self, tearoff=0, relief=tk.FLAT)
        self.configure(menu=self.menubar)

        # create menu file
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Archivo', menu=self.filemenu)
        self.filemenu.add_command(
            label='Copiar', 
            command=None, 
            accelerator='Ctrl+C', 
            image=self.img_copy, 
            compound=tk.LEFT
        )
        self.filemenu.add_command(
            label='Pegar', 
            command=None, 
            accelerator='Ctrl+V', 
            image=self.img_paste, 
            compound=tk.LEFT
        )
        self.filemenu.add_command(
            label='Deshacer', 
            command=None, 
            accelerator='Ctrl+Z', 
            image=self.img_undo, 
            compound=tk.LEFT
        )
        self.filemenu.add_command(
            label='Rehacer', 
            command=None, 
            accelerator='Ctrl+Y', 
            image=self.img_redo, 
            compound=tk.LEFT
        )
        self.filemenu.add_separator()
        self.filemenu.add_command(
            label='Preferencias', 
            command=None, 
            image=self.img_preferences, 
            compound=tk.LEFT
        )
        self.filemenu.add_separator()
        self.filemenu.add_command(
            label='Salir', 
            command=self.quit, 
            accelerator='Ctrl+Q', 
            image=self.img_exit, 
            compound=tk.LEFT
        )

        # create menu help
        self.ayudamenu = tk.Menu(
            self.menubar, 
            tearoff=0
        )
        self.menubar.add_cascade(
            label='Ayuda', 
            menu=self.ayudamenu
        )
        self.ayudamenu.add_command(
            label='Ayuda', 
            command=None, 
            image=self.img_help, 
            accelerator='F1', 
            compound=tk.LEFT
        )
        self.ayudamenu.add_command(
            label='Acerca de', 
            command=self.window_about, 
            image=self.img_about, 
            compound=tk.LEFT
        )

        # create display frame
        self.frm_display = ttk.Frame(self)
        self.frm_display.grid(row=0, column=0, padx=5, pady=5)

        # row 0: display
        self.ety_display = tk.Entry(
            self.frm_display, 
            # bind instance to widget
            textvariable=self.var_display, 
            width=21, # 17 
            justify=tk.RIGHT, 
            takefocus=False,
            font=('Consola', 20, 'bold'),
            background='#282828',
            foreground='#FFFFE0',
            relief='flat'
        )
        self.ety_display.grid(row=0, column=0, columnspan=6, ipady=20)

        # row 1: buttons frame
        self.frm_buttons = ttk.Frame(self)
        self.frm_buttons.grid(row=1, column=0, padx=5, pady=5)

        # horizontal and vertical inner margin
        IPADX=6 
        IPADY=15

        # buttons style
        ttk.Style().configure(
            'TButton', 
            font=('Helvetica', 11),
            width=5,
            background='#FFFFE0',
        )

        # row 1
        self.btn_seven = ttk.Button(self.frm_buttons, text='7', 
            command=lambda: self.controller.on_click_button('7')
            ).grid(row=1, column=0, ipadx=IPADX, ipady=IPADY)
        self.btn_eight = ttk.Button(self.frm_buttons, text='8', 
            command=lambda: self.controller.on_click_button('8')
            ).grid(row=1, column=1, ipadx=IPADX, ipady=IPADY)
        self.btn_nine = ttk.Button(self.frm_buttons, text='9',
            command=lambda: self.controller.on_click_button('9')
            ).grid(row=1, column=2, ipadx=IPADX, ipady=IPADY)
        self.btn_div = ttk.Button(self.frm_buttons, text='÷',
            command=lambda: self.controller.on_click_button('÷')
            ).grid(row=1, column=3, ipadx=IPADX, ipady=IPADY)
        self.btn_square = ttk.Button(self.frm_buttons, text='x²', 
            command=lambda: self.controller.on_click_button('\u00b2')
            ).grid(row=1, column=4, ipadx=IPADX, ipady=IPADY)

        # row 2
        self.btn_four = ttk.Button(self.frm_buttons, text='4',
            command=lambda: self.controller.on_click_button('4')
            ).grid(row=2, column=0, ipadx=IPADX, ipady=IPADY)
        self.btn_five = ttk.Button(self.frm_buttons, text='5',
            command=lambda: self.controller.on_click_button('5')
            ).grid(row=2, column=1, ipadx=IPADX, ipady=IPADY)
        self.btn_six = ttk.Button(self.frm_buttons, text='6',  
            command=lambda: self.controller.on_click_button('6')
            ).grid(row=2, column=2, ipadx=IPADX, ipady=IPADY)
        self.btn_mul = ttk.Button(self.frm_buttons, text='x',  
            command=lambda: self.controller.on_click_button('x')
            ).grid(row=2, column=3, ipadx=IPADX, ipady=IPADY)
        ttk.Button(self.frm_buttons, text='x⁻¹', 
            command=lambda: self.controller.on_click_button('⁻¹')
            ).grid(row=2, column=4, ipadx=IPADX, ipady=IPADY)
        
        # row 3
        self.btn_one = ttk.Button(self.frm_buttons, text='1',  
            command=lambda: self.controller.on_click_button('1')
            ).grid(row=3, column=0, ipadx=IPADX, ipady=IPADY)
        self.btn_two = ttk.Button(self.frm_buttons, text='2',  
            command=lambda: self.controller.on_click_button('2')
            ).grid(row=3, column=1, ipadx=IPADX, ipady=IPADY)
        self.btn_three = ttk.Button(self.frm_buttons, text='3', 
            command=lambda: self.controller.on_click_button('3')
            ).grid(row=3, column=2, ipadx=IPADX, ipady=IPADY)
        self.btn_sub = ttk.Button(self.frm_buttons, text='-',  
            command=lambda: self.controller.on_click_button('-')
            ).grid(row=3, column=3, ipadx=IPADX, ipady=IPADY)
        self.btn_square_root = ttk.Button(self.frm_buttons, text='√x', 
            command=lambda: self.controller.on_click_button('\u00bd')
            ).grid(row=3, column=4, ipadx=IPADX, ipady=IPADY)

        # row 4
        self.btn_zero = ttk.Button(self.frm_buttons, text='0',  
            command=lambda: self.controller.on_click_button('0')
            ).grid(row=4, column=0, ipadx=IPADX, ipady=IPADY)
        self.btn_dot = ttk.Button(self.frm_buttons, text=',',  
            command=lambda: self.controller.on_click_button(',')
            ).grid(row=4, column=1, ipadx=IPADX, ipady=IPADY)
        self.btn_per = ttk.Button(self.frm_buttons, text='%',  
            command=lambda: self.controller.on_click_button('%')
            ).grid(row=4, column=2, ipadx=IPADX, ipady=IPADY)
        self.btn_add = ttk.Button(self.frm_buttons, text='+',  
            command=lambda: self.controller.on_click_button('+')
            ).grid(row=4, column=3, ipadx=IPADX, ipady=IPADY)
        self.btn_factorial = ttk.Button(self.frm_buttons, text='x!',  
            command=lambda: self.controller.on_click_button('!')
            ).grid(row=4, column=4, ipadx=IPADX, ipady=IPADY)

        # row 5
        self.btn_clear = ttk.Button(self.frm_buttons, text='C', 
            command=lambda: self.controller.on_click_function('C')
            ).grid(row=5, column=0, ipadx=IPADX, ipady=IPADY)
        self.btn_undo = ttk.Button(self.frm_buttons, text='🠔', 
            command=lambda: self.controller.on_click_function('🠔')
            ).grid(row=5, column=1, ipadx=IPADX, ipady=IPADY)
        self.btn_rig_par = ttk.Button(self.frm_buttons, text='(', 
            command=lambda: self.controller.on_click_button('(')
            ).grid(row=5, column=2, ipadx=IPADX, ipady=IPADY)
        self.btn_lef_par = ttk.Button(self.frm_buttons, text=')', 
            command=lambda: self.controller.on_click_button(')')
            ).grid(row=5, column=3, ipadx=IPADX, ipady=IPADY)
        self.btn_equals = ttk.Button(self.frm_buttons, text='=', 
            command=lambda: self.controller.on_click_function('=')
            ).grid(row=5, column=4, ipadx=IPADX, ipady=IPADY)


    def center_window(self, w, h):
        """ Center window on the screen
			:param w: width window
			:param h: height window
		"""
        x = (self.winfo_screenwidth() - w) / 2
        y = (self.winfo_screenheight() - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def start_mainloop(self):
        """ Run the main window loop """
        self.mainloop()


    def window_about(self):
        """ Shows about window """
        about = About(self)
        about.mainloop()
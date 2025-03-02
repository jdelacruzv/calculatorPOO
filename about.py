"""
    Author: José De La Cruz
    Created: 2019-09-01
    Modified: 2021-04-23
"""
import tkinter as tk
import datetime as dt
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from utils import Utils


class About(tk.Toplevel):
	"""About popup widow to display Holybible general application description"""
	def __init__(self, master):
		super().__init__(master)
		self.transient(master)		# make the window transient(transitorio)
		self.grab_set()				# make the window modal
		self.title('Acerca de Calculator')
		self.resizable(False, False)
		self.protocol("WM_DELETE_WINDOW", self.close)
		self.utils = Utils()
		self.center_window(640, 500)
		self.focus_set()

		# main notebook
		self.nb_about = ttk.Notebook(self)
		self.nb_about.pack(side=tk.TOP, padx=5)

		# frame for information tab
		self.tab_info = ttk.Frame(self.nb_about)
		self.nb_about.add(self.tab_info, text='Información')
		self.nb_about.pack(fill=tk.BOTH, expand=tk.YES)

		self.img_about = tk.PhotoImage(file='asset/images/calculator.png')
		ttk.Label(self.tab_info, image=self.img_about).pack(side=tk.TOP, pady=30)

		self.lbl_title_info = ttk.Label(self.tab_info, text='Calculator 1.0.0')
		self.lbl_title_info.pack(side=tk.TOP)
		self.lbl_title_info.configure(font=('Helvatica', 20, 'bold'))

		syst = self.utils.platform_system_desc()  							  # get OS description
		lang = '\nPython {}'.format(self.utils.get_python_version_string())   # get Python version
		#lib = '\nTk {}'. format(self.utils.get_tk_version_str())
		lib = '\nTk {}'.format(self.tk.call('info', 'patchlevel'))			  # get Tk version

		self.lbl_platform_system = ttk.Label(self.tab_info, justify=tk.CENTER, text="{} {} {}". format(syst, lang, lib))
		self.lbl_platform_system.pack(side=tk.TOP, pady=30)
		self.lbl_platform_system.configure(font=('Helvatica', 10))

		current_year = dt.datetime.now().year
		txt = f'Copyright (c) 2019-{current_year} José De La Cruz \n @Todos los derechos reservados'
		self.lbl_right_info = ttk.Label(self.tab_info, text=txt, justify=tk.CENTER)
		self.lbl_right_info.pack(side=tk.TOP)
		self.lbl_right_info.configure(font=('Helvatica', 10))

		# frame for credit tab
		self.tab_credit = ttk.Frame(self.nb_about)
		self.nb_about.add(self.tab_credit, text='Créditos')
		self.nb_about.pack(fill=tk.BOTH, expand=tk.YES)
		
		self.lbl_title_credit = ttk.Label(self.tab_credit, text='Desarrolladores')
		self.lbl_title_credit.pack(padx=20, pady=30)
		self.lbl_title_credit.configure(font=('Helvatica', 20, 'bold'))

		self.lbl_name_credit1 = ttk.Label(self.tab_credit, text='José De La Cruz')
		self.lbl_name_credit1.pack()
		self.lbl_name_credit1.configure(font=('Verdana', 10, 'bold'))

		self.lbl_email_credit1 = ttk.Label(self.tab_credit, text='<jldlcv@gmail.com>')
		self.lbl_email_credit1.pack()
		self.lbl_email_credit1.configure(font=('Verdana', 10))

		# set horizontal separator bar to white
		ttk.Label(self.tab_credit, text='').pack(side=tk.TOP)

		self.lbl_name_credit2 = ttk.Label(self.tab_credit, text='Luis Castillo')
		self.lbl_name_credit2.pack()
		self.lbl_name_credit2.configure(font=('Verdana', 10, 'bold'))

		self.lbl_email_credit2 = ttk.Label(self.tab_credit, text='<lcastillovillena@gmail.com>')
		self.lbl_email_credit2.pack()
		self.lbl_email_credit2.configure(font=('Verdana', 10))

		# set horizontal separator bar to white
		ttk.Label(self.tab_credit, text='').pack(side=tk.TOP)

		self.lbl_name_credit3 = ttk.Label(self.tab_credit, text='Gloria Sánchez')
		self.lbl_name_credit3.pack()
		self.lbl_name_credit3.configure(font=('Verdana', 10, 'bold'))

		self.lbl_email_credit3 = ttk.Label(self.tab_credit, text='<glorypaty247@gmail.com>')
		self.lbl_email_credit3.pack()
		self.lbl_email_credit3.configure(font=('Verdana', 10))

		# set horizontal separator bar to white
		ttk.Label(self.tab_credit, text='').pack(side=tk.TOP)

		self.lbl_name_credit4 = ttk.Label(self.tab_credit, text='Stefano De La Cruz')
		self.lbl_name_credit4.pack()
		self.lbl_name_credit4.configure(font=('Verdana', 10, 'bold'))

		self.lbl_email_credit4 = ttk.Label(self.tab_credit, text='<delacruzstefano27@gmail.com>')
		self.lbl_email_credit4.pack()
		self.lbl_email_credit4.configure(font=('Verdana', 10))

		# frame for license tab
		self.tab_license = ttk.Frame(self.nb_about)
		self.nb_about.add(self.tab_license, text='Licencia')
		self.nb_about.pack(fill=tk.BOTH, expand=tk.YES)

		self.txt_license = ScrolledText(self.tab_license, undo=True, wrap=tk.WORD, height=27) # width=80
		self.txt_license.pack(side=tk.LEFT)
		self.txt_license.insert('1.0', self.utils.open_text_file('asset/txt/license.txt'))
		# make text widget 'read-only'
		self.txt_license.configure(state=tk.DISABLED)


	def center_window(self, w, h):
		"""Center window"""
		x = (self.winfo_screenwidth() - w) / 2
		y = (self.winfo_screenheight() - h) / 2
		self.geometry('%dx%d+%d+%d' % (w, h, x, y))


	def close(self):
		"""Close window"""
		self.master.focus_set()
		self.destroy()
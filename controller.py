"""
    A simple calculator with basic operations and a menu of options (OOP).

    Author: José De La Cruz
    Created: 2019-08-04
"""
from calculator import Calculator
from gui import Gui


class Controller:
    """Class that works as the application controller"""

    def __init__(self):
        self.calculator = Calculator()
        self.gui = Gui(self)


    def on_click_button(self, caption):
        """Send the clicks given by the user to the Calculator class"""
        result = self.calculator.operations(caption)
        self.gui.var_display.set(result)


    def on_click_function(self, func):
        """Call the functions: equal, clean or undo of the Calculator class"""
        if func == '=':
            result = self.calculator.button_equals()
            self.gui.var_display.set(result)
        elif func == 'Limpiar':
            self.gui.var_display.set('')
        elif func == 'Deshacer':
            result = self.calculator.button_undo()
            self.gui.var_display.set(result)
            print(result)


    def start_gui(self):
        """Call method Gui class"""
        self.gui.start_mainloop()
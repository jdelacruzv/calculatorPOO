from calculator import Calculator
from gui import Gui


class Controller:
    """ Class that works as the application controller """
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.gui = Gui(self)
    

    def start_gui(self):
        """ Call method Gui class """
        self.gui.start_mainloop()


    def on_click_button(self, caption):
        """ Send the clicks given by the user to the Calculator class """
        result = self.calculator.click_button(caption)
        # set(update) value to widget
        self.gui.var_display.set(result)


    def on_click_function(self, func):
        """ Call the functions: equal, clean, undo or factorial of the Calculator class """
        if func == '=':
            result = self.calculator.equals_button()
            self.gui.var_display.set(result)
        elif func == 'C':
            result = self.calculator.clear_button()
            self.gui.var_display.set(result)
        elif func == '🠔':
            result = self.calculator.undo_button()
            self.gui.var_display.set(result)
        else:
            result = 'Function error'
            self.gui.var_display.set(result)
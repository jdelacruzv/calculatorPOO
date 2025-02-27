"""
    A simple calculator with basic operations and a menu of options (OOP).

    Author: José De La Cruz
    Created: 2019-08-04
    Modified: 2025-02-27
"""
import math


class Calculator:
    """Class that works as the application model"""

    def __init__(self):
        self.value = ''
        

    def click_button(self, caption): 
        """Insert the clicks given by the user (numbers and symbols)"""
        self.value += caption
        return self.value


    def clear_button(self):
        """Clean text box"""
        self.value = ''
        return self.value


    def undo_button(self):
        """Delete the last character and/or number entered"""
        if self.value != '':
            cadena = len(self.value)
            self.value = self.value[:cadena - 1]
            return self.value
        else:
            return 'No hay datos'


    def replace_button(self):
        """Replace 'x' by '*' and '÷' by '/'"""
        if self.value != '':
            temp = self.value.replace('÷', '/')
            temp = temp.replace('x', '*')
            temp = temp.replace(',', '.')
            temp = temp.replace('%', '/100')
            temp = temp.replace('\u00b2', '**2')
            temp = temp.replace('\u00bd', '**(1/2)')
            self.value = temp.replace('⁻¹', '**-1')
        return self.value


    @staticmethod
    def replace_point_result(val):
        """Replace point by comma of the final result"""
        return str(val).replace('.', ',')


    @staticmethod
    def decimal_or_integer(result):
        """Returns the integer part of the final result"""
        try:
            decimal, entera = math.modf(result)
            if decimal == 0.0:
                return int(entera)
            else:
                return result
        except:
            return 'Expresión incorrecta'


    def equals_button(self):
        """Perform the data operation"""
        self.replace_button()
        res = None
        try:
            res = eval(self.value)
        except:
            res = 'ERROR'
        finally:
            self.value = self.replace_point_result(
                self.decimal_or_integer(res))
        return self.value
    

    def factorial_button(n):
        # n = int(n)
        # if n == 0 or n == 1:
        #     return 1
        # else:
        #     return n * factorial(n-1)
        return math.factorial(n)
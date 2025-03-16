import math


class Calculator:
    """Class that works as the application model"""
    def __init__(self):
        self.value = ''
        

    def click_button(self, caption): 
        """ Insert the clicks given by the user (numbers and symbols) """
        self.value += caption
        return self.value


    def clear_button(self):
        """ Clean text box """
        self.value = ''
        return self.value


    def undo_button(self):
        """ Delete the last character and/or number entered """
        if self.value != '':
            char_chain = len(self.value)
            self.value = self.value[:char_chain - 1]
            return self.value
        else:
            return ''


    def replace_button(self):
        """ Replace 'x' by '*' and '÷' by '/' """
        if self.value != '':
            temp = self.value.replace('÷', '/')
            temp = temp.replace('x', '*')
            temp = temp.replace(',', '.')
            temp = temp.replace('%', '/100')
            temp = temp.replace('\u00b2', '**2')
            temp = temp.replace('⁻¹', '**-1')
            self.value = temp.replace('\u00bd', '**(1/2)')
        return self.value


    @staticmethod
    def replace_point_result(val):
        """ Replace point by comma of the final result """
        return str(val).replace('.', ',')


    @staticmethod
    def decimal_or_integer(result):
        """ Returns the integer part of the final result """
        try:
            dec_part, int_part = math.modf(result)
            if dec_part == 0.0:
                return int(int_part)
            else:
                return result
        except:
            return 'Error'


    def equals_button(self):
        """ Perform the data operation """
        self.replace_button()
        result = None
        try:
            # TODO: 3!+5=11 o 5+3!=11
            if '!' in self.value: 
                temp = int(self.value.replace('!', ''))
                self.value = str(math.factorial(temp))
            result = eval(self.value)
        except:
            result = 'Error'
        finally:
            self.value = self.replace_point_result(self.decimal_or_integer(result))
        return self.value
# module import exercise
# using functions built inside it
#
# currently coded in temp_module:
#
# def calc_to_fahr (Fahr):
#   Fahrenheit = Fahr * 9/5 + 32
#   return Fahrenheit
#
# def calc_to_cels (Cels):
#   Celsius = (Cels - 32) * 5/9
#   return Celsius
#
#

import temp_module

print (temp_module.calc_to_cels(212))               # note - does not require using the same arbitrary word as the module function uses.
                                                    # for example, calc_to_cels function in temp_module.py uses string 'Cels'
print (temp_module.calc_to_fahr(100))

print ()

from tuple_vs_list import pond

print (pond['blah', 'blah', 'blah'])


from tuple_vs_list import *                         # import all code

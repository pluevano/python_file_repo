# python module that calculates both Fahrenheit and Celsius
#

def calc_to_fahr (Fahr):
  Fahrenheit = Fahr * 9/5 + 32
  return Fahrenheit

def calc_to_cels (Cels):
  Celsius = (Cels - 32) * 5/9
  return Celsius

def main ():
    tmp1 = (0, 34, 212)
    for temp in tmp1:
        print (temp, 'degrees Fahrenheit =', round(calc_to_cels(temp)), 'degrees Celsius')
        print ()

    tmp2 = (0, 34, 112)
    for temp in tmp2:
        print (temp, 'degrees Celsius =', round(calc_to_fahr(temp)), 'degrees Fahrenheit')
        print()

if __name__ == '__main__':
  main()

import sys                                      # prints out current python search dir list
from pprint import pprint as print
print (sys.path)

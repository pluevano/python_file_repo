# calculator using functions
#
print ('This program will calculate the total cost of a loan with a given APR.')

def main_calulation(month_invest, year_int, years):




def main():
    usage = 'u'


    while usage == 'u':
        int_total = 0
        print ()
        loan = float(input('What is the loan amount? \t'))
        interest = float(input('What is the interest rate?\t'))
        duration = int(input('What is the duration of loan in years?\t'))

        for num in range (duration):
            int_total += (loan * (interest/100))


if __name__ == __main__:
    main()

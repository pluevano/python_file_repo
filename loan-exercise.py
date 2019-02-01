# while loop for repeated usage of calculation program
#

usage = 'u'
print ('This program will calculate total cost of a loan with a given APR.')

while usage == 'u':
    int_total = 0
    print ()
    loan = float(input('What is the loan amount? \t'))
    interest = float(input('What is the interest rate?\t'))
    duration = int(input('What is the duration of loan in years?\t'))

    for num in range (duration):
        int_total += (loan * (interest/100))

    print ()
    print ('The total interest paid on this loan is $' ,int_total)
    print ('The total cost of this loan is $' ,(int_total + loan))
    print ()
    retry = input('Do you wish to run this program again, y/n?\t')
    if retry == 'n':
        usage = retry
    elif retry == 'y':
        usage = usage
    else:
         retry = input('Do you wish to run this program again, y/n?\t')

print ()
print ('Good luck with your loan!')

#for loop with break
#
#
data = [47, "Paul", "Smith", 89]
score = [121, 3.9, "FE"]
print (data + score [2:3])
print ()
print (score + data [1:])
print ()

def pond(xyz):
    '''This is one way to make a function'''        #document string for writing description in function
    xyz += ('blah', 'blah', 'blah')
    return xyz


tuple1 = (1, 2, 3)      # tuples require ()
list3 = pond(tuple1)
print (list3)


list1 = [4, 5, 6]       # lists require []
print (list1)
print ()



vehicle = ['chevy', 'ford']
print (vehicle[0], vehicle[1])

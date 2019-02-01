#for loop with break
#
#
data = [121, 'Paul', 'Smith']
score = [121, 3.9]
print (data + score [1:2])

print (score + data [0:])

def pend(xyz):
    '''This is one way to make a function'''
    xyz += ('blah', 'blah', 'blah')
    return xyz


tuple1 = (1, 2, 3)      # tuples require ()
list1 = [4, 5, 6]       # lists require []
#list2 = pend(list1)
list3 = pend(tuple1)

print (list1)
#print (list2)
print (list3)

vehicle = ['chevy', 'ford']
print (vehicle[0], vehicle[1])

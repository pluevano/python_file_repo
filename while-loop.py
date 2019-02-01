#basic while loop
#
#

v = 0

while v < 10:
    v += 1
    print ('i am', v)
print ('i am done counting')


#basic for loop
#
#
word = 'calculus'
for chars in word:
    print (chars)

levels = ['calculus', 'geometry', 'trigonometry', 'algebra']
for level in levels:
    print (level)

for num in range (11):
    print (num)

words = ['sid', 'nancy', 'john', 'mike', 'rich']
for num in range (5):
    print (words[num])

for num in range(len(words)):                                     #built-in function <len> is used to find size of list
    print (words[num])

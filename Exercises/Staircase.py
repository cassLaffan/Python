import math

def staircase(n):
    '''
    (int) -> str

    Prints a 'staircase' of "*', the number of steps determined by the integer
    n.

    >>>staircase(4)
        *
       **
      ***
     ****

    >>>staircase(0)


    '''

    m = ''

    i = 1
    n = int(n)

    while i < n:
        m += (n - i) * ' ' + i * '*' + '\n'
        i += 1

    m += i * '*'



    print(m)


#Question #2

def alphabetize(namelist):
    '''
    (list) -> list

    Returns a list of aphabetized names by last name, given and returned in the
    format of firstName lastName.

    >>>alphabetize(['John Jacobs', 'Karen Smith', 'Xavier Latos'])
    John Jacobs
    Xavier Latos
    Karen Smith

    >>>alphabetized([])

    '''

    listoflast = []
    alphabetized = ''

    for item in namelist:
        newitem = item.split()
        listoflast.append(newitem[1])

    newlist = sorted(listoflast)

    for name in newlist:
        for item in namelist:
            if name in item:
                alphabetized += str(item) + '\n'

    newalpha = alphabetized.strip('\n')

    print(newalpha)


#Question #3

def calculateE(n):
    '''
    (int) -> float

    Returns an approximate value of e, using the infinite series of 1/n!

    >>>calculateE(3)
    2.6666666666666667

    >>>calculateE(1)
    2.0
    '''

    e = 1

    n = int(n)

    while n != 0:
        e = e + (1/float(math.factorial(n)))
        n = n - 1

    return e

#Question #4

def giveoccuringitems(items):
    '''
    (list) -> Str

    Returns a string of all the reoccuring values in items, each value only
    listed once.

    >>>giveoccuringitems([1, 4, 3, 3, 2, 5, 3])
    '3'

    >>>giveoccuringitems(['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'])
    'a, b, c, d'

    '''

    repeatstring = ''
    i = 0

    while i != len(items):
        for j in range(len(items) -1):
            if (i !=j) and items[i] == items[j]:
                if str(items[i]) not in repeatstring:
                    repeatstring += str(items[i]) + ', '
        i += 1

    final = repeatstring.strip(' ')
    finalstring = final.strip(',')

    return finalstring


if __name__ == '__main__':

    question = raw_input('What would you like to do? Staircase, Alphabetize, Calculate e or Repeat String?')

    if question == 'Staircase':
        n = input('What n would you like?')
        print(staircase(n))
    if question == 'Alphabetize':
        namelist = input('What is your namelist?')
        print(alphabetize(namelist))
    if question == 'Calculate e':
        n = input('To what number?')
        print(calculateE(n))
    if question == 'Repeat String':
        string = 'What list of strings?'
        print(giveoccuringitems(string))

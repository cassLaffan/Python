def veggielist(veggies):
    '''
    (list of str) -> str

    The program takes a list of vegetables, as given by the user input,
    then outputs a string called 'diet', where the vegetables are listed with
    a '+' in between each vegetable.

    >>>veggielist(['Carrots', 'Spinach', 'Lettuce'])
    Diet: Carrots + Spinach + Lettuce

    >>>veggielist([])
    Diet:

    '''
    veggiediet = 'Diet: '

    for item in veggies:
        if item != veggies[-1]:
            veggiediet = veggiediet + item + ' + '
        else: veggiediet += item

    return veggiediet

## Question 2

def getsortedname(name):
    '''
    (str) -> str

    Returns name, which is given in the format of 'Firstname Middlename
    Lastname', as a string of the format 'Firstname MiddleInitial. Lastname'.

    >>>getsortedname('John Jakob Jingleheimershmit')
    John J. Jingleheimershmit

    >>>getsortedname('Cassandra Frances Laffan')
    Cassandra F. Laffan

    '''

    newname = name.split()

    newername  = ''

    for item in newname:
        if newname.index(item) != 1:
            newername += item + ' '

        else:
            newername += item[0] + '.' + ' '

    return newername

##Question 3

def fancydate(numericdate):
    '''
    (str) -> str

    Returns the date, which is given in the form MM/DD/YYYY, in the format
    Day Month Year.

    >>>fancydate('10/27/1994')
    27 October 1994

    >>>fancydate('01/01/2001')
    1 January 2001
    '''

    daylist = numericdate.split('/')

    montdict ={'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05':\
         'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September',\
         '10': 'October', '11': 'November', '12': 'December'}

    emptydate = daylist[1] + ' ' + montdict[daylist[0]] + ' ' + daylist[2]

    return emptydate

##Question 4

def howmanydays(date):
    '''
    (str) -> int

    Returns the number of days the given date is into the year.
    (out of 365 days)

    >>>howmanydays('May 5')
    125

    >>>howmanydays('January 1')
    1

    '''

    Year = [['January', 31], ['February', 28], ['March', 31], ['April', 30],\
            ['May',31], ['June', 30], ['July', 31], ['August', 31],\
            ['September', 30], ['October', 31],['November', 30],\
            ['December', 31]]


    monthnum = 0

    monthlist = date.split()

    for item in Year:
        if monthlist[0] in item:
            n = Year.index(item) - 1
            while n != -1:
                Chep = int(Year[n][1])
                monthnum += Chep
                n -= 1

    monthnum += int(monthlist[1])

    return monthnum

if __name__ == '__main__':
    action = input('What would you like to do? Please enter one of the following:\
    "Make a Diet", "Shorten my Name", "Organize the Date" or "How many Days?"')

    if action == 'Make a Diet':
        numofveg = input('How many veggies would you like in your diet?')
        n = 1
        vegetablelist = []
        r = int(numofveg)
        while n != r + 1:
            veggie = input('What kind of vegetable?')
            vegetablelist.append(veggie)
            n += 1
        print(str(veggielist(vegetablelist)))

    if action == 'Shorten my Name':
        name = input('What is your name? Enter in the format:"Firstname Middlename Lastname"')
        print(str(getsortedname(name)))

    if action == 'Organize the Date':
        date = input('What is the date? Enter in format "Month Day Year"')
        print(str(fancydate(date)))

    if action == 'How many Days?':
            date = input('Please enter a Month and Day. Exmaple: "January 1"')
            print(str(howmanydays(date)) + ' days')


    else:
        print('Invalid input. Please try again.')

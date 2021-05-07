import numpy as np
import matplotlib.pyplot as plt
import csv, sqlite3

conn = sqlite3.connect('sales.db')

def importData():
    #Create table:
    conn.execute('CREATE TABLE IF NOT EXISTS \
            salesTable(ID INTEGER PRIMARY KEY AUTOINCREMENT, MonthYear TEXT, \
            Store TEXT, Product TEXT, Sales INT, Expense INT, Price INT, Profit INT)')
    
    #Import data from csv:
    with open('All.csv','rb') as fin: # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['MonthYear'], i['Store'], i['Product'], i['Sales'], i['Expense'], i['Price'], i['Profit']) for i in dr]
    cur = conn.cursor()
    cur.executemany("INSERT INTO salesTable(MonthYear, Store, Product, Sales, Expense, Price, Profit) VALUES (?,?,?,?,?,?,?);", to_db)

    #Check that data is present:
    cursor = conn.execute("SELECT * from salesTable")
    rows = cursor.fetchall()
    print(rows)
    print('data imported')

def plotMulti(columnVar):
    #Plot columnVar per month per store side-by-side:
    N = 3
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27       # the width of the bars

    fig = plt.figure(1)
    ax = fig.add_subplot(111) 

    #red bars: store A in Jan, Feb, Mar
    commandA = 'SELECT sum({}) AS "totA" \
    FROM salesTable WHERE Store = "A" GROUP BY MonthYear ORDER BY ID'.format(columnVar)
    CursorA = conn.execute(commandA)
    yvals = CursorA.fetchall()
    yvals = [i[0] for i in yvals]
    rects1 = ax.bar(ind, yvals, width, color='r')

    #green bars: store B in Jan, Feb, Mar
    commandB='SELECT sum({}) AS "totB" \
    FROM salesTable WHERE Store = "B" GROUP BY MonthYear ORDER BY ID'.format(columnVar)
    CursorB = conn.execute(commandB)
    zvals = CursorB.fetchall()
    zvals = [i[0] for i in zvals]
    rects2 = ax.bar(ind+width, zvals, width, color='g')

    #blue bars: store C in Jan, Feb, Mar
    commandC='SELECT sum({}) AS "totC" \
    FROM salesTable WHERE Store = "C" GROUP BY MonthYear ORDER BY ID'.format(columnVar)
    CursorC = conn.execute(commandC)
    kvals = CursorC.fetchall()
    kvals = [i[0] for i in kvals]
    rects3 = ax.bar(ind+width*2, kvals, width, color='b')

    if columnVar=='Sales':
        ax.set_ylabel('No. of Sales')
    elif columnVar=='Profit':
        ax.set_ylabel('Profit ($)')
    ax.set_xticks(ind+1.5*width)
    ax.set_xticklabels( ('2016-Jan', '2016-Feb', '2016-Mar') )
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend((rects1[0], rects2[0], rects3[0]), ('Store A', 'Store B', 'Store C'), 
              loc='center left', bbox_to_anchor=(1, 0.5))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.01*h, '{}'.format(int(h)),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.show()

def options():
    # Print out the options
    print '\nPlease make a selection. First import data.'
    print '1. Import Data'
    print '2. View Sales Per Month Per Store'
    print '3. View Profit Per Month Per Store'
    print '4. Exit'
    
    # Ask user what they want to do
    response = raw_input('Enter number: ')

    # Check the user response
    if response == '1':
        importData()
    elif response == '2':
        global x
        x="Sales"
        plotMulti(x)
    elif response == '3':
        global y
        y="Profit"
        plotMulti(y)
    else:
        print 'Exiting the program'
        return

def mainLoop():
    in_loop = True
    while in_loop == True:
        # Run options function
        options()
        # Ask user if they want to continue
        again = raw_input(\
        'Would you like to do something else? (y/n) ')
        # if answer does not equal 'y', exit loop
        if again != 'y':
            in_loop = False

mainLoop()

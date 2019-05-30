from graphics import * 
## the graphics.py file contain all the Graph module
def main():
    ######## Introduction ########
    print("This program plots the growth of a 10 year investment.")
    
    # Get principal and investemtent rate 
    principal = input("Enter the initial principal:")
    principal = int(principal)
    rate = input("Enter the annualized interest rate:")
    rate = float(rate)

    #Create a graphcs window with label left edge 
    win = GraphWin("Investement Growth Chart", 350, 240)
    win.setBackground("white")

    ## the first label is center at the point 20 for the x line (0-->320) 
        # and 10 (starting from 240 which is 230) so we give a margin of 10 
    ## Every other label follow the same format(change occured only one the y line)
        # where we move from down to up on 50 pixel unit
    Text(Point(20, 230), '0.0K').draw(win)
    Text(Point(20, 180), '2.5K').draw(win)
    Text(Point(20, 130), '5.0K').draw(win)
    Text(Point(20, 80), '7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)
    ### Draw bar for initial principal 
        # we give 50 pixel for $2,500 --> 0.02 for $1
        # the initial bar has a principal of #2000 --> have to move from 230 to 
            # (230-princil*0.02) on the y line going up (note that our 0 start at 240pixel on the y line)
        # on the x side 20+20 use for the label and magin --> We have 320-40 = 280 left for 11 bar 
            # that give us an average of 280/11 = 25 pixel on average for each bar
        # the initial bar move from the left(which start from 40) to right(40+25= 65) for 25 pixel 
    height = principal * 0.02
    bar = Rectangle(Point(40,230), Point(65,230-height))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)

    ### Drawing bar for the following year 
        # before that we got the following algothim: 
            # for each year we move 25 to right and principal*0.02 up, but principal change each year
            # for year going from a 1 to 10 
                # we get the new principal = principal * (1+apr)
                # the get the new pixel for the x line to start drawing the bar from = 25*year +40
    for year in range(1,11):
        # get value for next year 
        principal = principal*(1+ rate)
        # draw bar for this value 
        xll = year*25 +40
        height =principal*0.02
        bar = Rectangle(Point(xll,230), Point(xll+65, 230-height))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)


    win.getMouse()
    win.close()


main()
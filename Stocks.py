__author__ = 'Robbie Barrat'
# I need the datetime module for telling the current date when I compare todays stock values to 5 days ago and such.
import datetime
import sys
# Yahoo Finance V. 1.1.4
from yahoo_finance import Share


# Checks to see if it is currently the weekend, and displays a message if so (since the stock market only operates on weekdays)
def weekend():
    if datetime.datetime.today().weekday() == 6:
        print "Hey, according to your computer it is Sunday, so the stock market is closed today."
        print "The data you see will be from the last time the stock market was opened."
    elif datetime.datetime.today().weekday() == 5:
        print "Hey, according to your computer it is Saturday, so the stock market is closed today."
        print "The data you see will be from the last time the stock market was opened."


# Just a nice greeting message#
def greeting():
    print "Enter the abbreviation of the company you'd like to look into, for example, 'Google' would be 'GOOGL'"
    takeinput()


# Here is the function that actually takes input #
def takeinput():
    company = raw_input("Company Abbreviation: ")
    if company == "":
        print "You need to enter a company name, buddy."
        takeinput()
    elif company.isalpha() == False:
        print "Try to keep it all letters, no numbers, spaces or symbols allowed."
        takeinput()
    else:
        print "Thank you, please wait a minute while the data for your company is being retrieved..."
    # the reason there are two variables for this (companyname and company) is because there were some issues with the program
    # using a bad input, so companyname is defined only if the input is correct and accepted.
        companyname = company
        recentdata(companyname)


# This function just gives some quick data about how the stock has been doing today. #
def recentdata(companyname):
    try:
        companydata = Share(companyname)
        print "This morning, it opened for $" + companydata.get_open() + ", and right now is at $" + companydata.get_price() + "."
        if companydata.get_open() > companydata.get_price():
           difference = float(companydata.get_open()) - float(companydata.get_price())
           if len(str(difference)) < 3:
               print "Since this morning, the price has fallen by $" + str(difference) + "0"
           else:
              print "Since this morning, the price has fallen by $" + str(difference)
        elif companydata.get_open() < companydata.get_price():
            difference = float(companydata.get_price()) - float(companydata.get_open())
            if len(str(difference)) < 3:
                print "Since this morning, the price has risen by $" + str(difference) + "0"
            else:
                print "Since this morning, the price has risen by $" + str(difference)
        print ""
        selection = raw_input(
            "Would you like some info about what the stock has been like in the past few days? Yes/No: ")
        if str.lower(selection) == "no":
            end()
        elif str.lower(selection) == "yes":
            print "Okay, please wait a moment"
    except (RuntimeError, TypeError, NameError):
        print "Whoops, something went wrong there. Are you sure you entered a valid company abbreviation?"

    finally:
        longterm(companyname)


def longterm(companyname):
    print "Calculating date stuffs..."
    # Format the date #
    datelist = []
    for i in str(datetime.datetime.today()):
        datelist.append(i)
    year = str(datelist[0] + datelist[1] + datelist[2] + datelist[3])
    month = str(datelist[5] + datelist[6])
    day = str(datelist[8] + datelist[9])
    dates(companyname, year, month, day)

# This huge, horrible function formats the date and takes care of issues that arrise if three days ago happened last
# month or last year (For example: we can't have July -1st, it would have to be June 30th)
# I know, I could've done better here -- I should've used a loop. Maybe I'll fix it if I ever do an update.
def dates(companyname, year, month, day):
    # These just assign the months certain amounts of days, so if 3 days ago was last month it won't freak out.
    january = 31
    # I hate leap years.
    if int(year) % 4 == 0:
        february = 29
    else:
        february = 28

    march = 31
    april = 30
    may = 31
    june = 30
    july = 31
    august = 31
    september = 30
    october = 31
    november = 30
    december = 31
    threedaysago = int(day) - 3
    twodaysago = int(day) - 2
    onedayago = int(day) - 1
    today = int(day)

    # THREE DAYS AGO#

    if threedaysago <= 0:
        threemonth = int(month) - 1

        # Incase 3 sdays ago happened to be last year...
        if int(month) == 0:
            threeyear = year - 1
            month = 12
            threedaysago = december + day - 3
        else:
            threeyear = year
        if month == 1:
            threedaysago = january + day - 3
        if month == 2:
            threedaysago = february + day - 3
        if month == 3:
            threedaysago = march + day - 3
        if month == 4:
            threedaysago = april + day - 3
        if month == 5:
            threedaysago = may + day - 3
        if month == 6:
            threedaysago = june + day - 3
        if month == 7:
            threedaysago = july + day - 3
        if month == 8:
            theedaysago = august + day - 3
        if month == 9:
            threedaysago = september + day - 3
        if month == 10:
            threedaysago = october + day - 3
        if month == 11:
            threedaysago = november + day - 3
    else:
        threemonth = month
        threeyear = year

    # TWO DAYS AGO#

    if twodaysago <= 0:
        twomonth = int(month) - 1

        # Incase two days ago happened to be last year...
        if int(month) == 0:
            twoyear = year - 1
            month = 12
            twodaysago = december + day - 2
        else:
            twoyear = year
        if month == 1:
            twodaysago = january + day - 2
        if month == 2:
            twodaysago = february + day - 2
        if month == 3:
            twodaysago = march + day - 2
        if month == 4:
            twodaysago = april + day - 2
        if month == 5:
            twodaysago = may + day - 2
        if month == 6:
            twodaysago = june + day - 2
        if month == 7:
            twodaysago = july + day - 2
        if month == 8:
            theedaysago = august + day - 2
        if month == 9:
            twodaysago = september + day - 2
        if month == 10:
            twodaysago = october + day - 2
        if month == 11:
            twodaysago = november + day - 2
    else:
        twomonth = month
        twoyear = year

    # ONE DAY AGO#

    if onedayago <= 0:
        onemonth = int(month) - 1
        # Incase one day ago was last year...
        if int(month) == 0:
            oneyear = year - 1
            month = 12
            onedayago = december + day - 1
        if month == 1:
            onedayago = january + day - 1
        if month == 2:
            onedayago = february + day - 1
        if month == 3:
            onedayago = march + day - 1
        if month == 4:
            onedayago = april + day - 1
        if month == 5:
            onedayago = may + day - 1
        if month == 6:
            onedayago = june + day - 1
        if month == 7:
            onedayago = july + day - 1
        if month == 8:
            theedaysago = august + day - 1
        if month == 9:
            onedayago = september + day - 1
        if month == 10:
            onedayago = october + day - 1
        if month == 11:
            onedayago = november + day - 1
    else:
        onemonth = month
        oneyear = year
    combine(onedayago, onemonth, oneyear, twodaysago, twomonth, twoyear, threedaysago, threemonth, threeyear, companyname)


# All this function does is put the data into a format that the yahoo_finance module can easily read.
def combine(onedayago, onemonth, oneyear, twodaysago, twomonth, twoyear, threedaysago, threemonth, threeyear, companyname):
    print "Analyzing data from the past few days..."
    fullone = str(oneyear) + "-" + str(onemonth) + "-" + str(onedayago)
    fulltwo = str(twoyear) + "-" + str(twomonth) + "-" + str(twodaysago)
    fullthree = str(threeyear) + "-" + str(threemonth) + "-" + str(threedaysago)


# Just gets the info and puts it into programmer friendly names
    def getclosing(date, company):
        # Thanks to stackoverflow user 'TessellatingHeckler' for helping me out with this next function! At the time dictionaries were a foreign concept to me.
        readings = company.get_historical(date, date)
        for reading in readings:
            close = reading['Close']
            return close

    company = Share(companyname)
    closingonedayago = getclosing(fullone, company)
    closingtwodaysago = getclosing(fulltwo, company)
    closingthreedaysago = getclosing(fullthree, company)
    twohundredavg = company.get_200day_moving_avg()
    fiftyavg = company.get_50day_moving_avg()
    today = company.get_price()
    decision(today, closingonedayago, closingtwodaysago, closingthreedaysago, twohundredavg, fiftyavg)


# All this does is get information, display it in a readable fasion, and then determine based on short term and long term
# data if the stock is worth investing in. It uses a system of points (titled positive and negative), which it ads up
# and uses to determine if the stock is overall 'good' or 'bad'. If you don't understand just look at the code.
def decision(today, oneday, twoday, threeday, twohundredavg, fiftyavg):
    # The 'negative' and 'positive' values will act like a score, and in the end will be used to determine an 'overall' score of good or bad.
    negative = 0
    positive = 0
    print "Today's price: " + str(today)
    print "Yesterday's price: " + str(oneday)
    print "Two days ago's price: " + str(twoday)
    print "Three days ago's price: " + str(threeday)
    print "Fifty day moving average: " + str(fiftyavg)
    print "Two hundred day moving average: " + str(twohundredavg)
    print ""
    print ""

    # These are just for doing short term stuff. Longer term stuff (50 and 200 day moving averages) comes 20 lines later

    if threeday > twoday and twoday > oneday and oneday > today:
        print "Over the span of 3 days ago and today, the price has been going down steadily."
        print "There is a %" + str(abs(float(threeday) / float(today))) + " difference between the price three days ago and today's price."
        negative += 2
    elif threeday > today:
        print "There have been some inconsistancies with the pattern, but today's price is lower than three day's ago."
        print "There is a %" + str(abs(float(threeday) / float(today))) + " difference between the price three days ago and today's price."
        negative += 1
    if threeday < twoday and twoday < oneday and oneday < today:
        print "Over the span of 3 days ago and today, the price has been going up steadily."
        print "There is a %" + str(abs(float(threeday) / float(today))) + " difference between the price three days ago and today's price."
        positive += 2
    elif threeday < today:
        print "There have been some inconsistancies with the pattern, but today's price is higher than three day's ago."
        print "There is a %" + str(abs(float(threeday) / float(today))) + " difference between the price three days ago and today's price."
        positive += 1

    # Now these are the longer term things #3
    if fiftyavg > twohundredavg:
        print "The fifty day average is greater than the two hundred day average, which signifies a longer term upwards trend."
        positive += 2
    elif fiftyavg < twohundredavg:
        print "The two hundred day average is greater than the fifty day average, which signifies a longer term downwards trend."
        negative += 2
    elif fiftyavg == twohundredavg:
        print "You probably didn't enter a valid company. Restart the program and try again."
        end()

    if negative > positive:
        if negative == 4:
            print "This stock looks like it is doing VERY poor! I wouldn't invest in it."
            end()
        if negative - positive == 1:
            print "This stock is doing slightly bad. It might recover in the near future, but for now I wouldn't buy it."
            end()
        print "This stock looks like it isn't doing well... I wouldn't invest in it."
        end()
    elif negative < positive:
        if positive == 4:
            print "This stock looks like it is doing very well! I would invest in it!"
            end()
        if positive - negative == 1:
            print "This stock is doing slightly good. It isn't making any serious growth at the moment."
            print "If you buy it you probably won't lose any money, but you probably won't make much either."
            end()
        print "This stock looks like it is doing pretty well. I suggest investing in it."
        end()
    elif positive == negative:
        print "This stock is doing mediocre. I would look for another stock to buy unless you are very confident in this one."
        end()


# Very simple function, just exits the program. and says goodbye to the user.
def end():
    print ""
    print "Alright, goodbye!"
    print "Press the 'return' or 'enter' key to exit..."
    pause = raw_input("")
    raise SystemExit("Bye")


### ---------------------------------------------------------------------------------------------------------------- ###
# This is just the part where it runs all the functions after they've been defined #

weekend()
greeting()

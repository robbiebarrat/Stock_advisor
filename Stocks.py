__author__ = 'Robbie Barrat'
# I need the datetime module for telling the current date when I compare todays stock values to 5 days ago and such.
import datetime
# Yahoo Finance V. 1.1.4
from yahoo_finance import Share
# Arrow -- replaced the old date module
import arrow


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
    elif not Share(str(company)).get_price():
        print "That isn't a valid company, pal."
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
    currentdate = arrow.utcnow()
    onedayago = currentdate.replace(days=-1).format('YYYY-MM-DD')
    twodaysago = currentdate.replace(days=-2).format('YYYY-MM-DD')
    threedaysago = currentdate.replace(days=-3).format('YYYY-MM-DD')
    fivedaysago = currentdate.replace(days=-5).format('YYYY-MM-DD')
    oneweekago = currentdate.replace(days=-7).format('YYYY-MM-DD')
    combine(onedayago, twodaysago, threedaysago, fivedaysago, oneweekago, companyname)


# All this function does is put the data into a format that the yahoo_finance module can easily read.
def combine(onedayago, twodaysago, threedaysago, fivedaysago, oneweekago, companyname):
    print "Analyzing data from the past few days..."
    dates = [onedayago, twodaysago, threedaysago, fivedaysago, oneweekago]
    for i in dates:
        i == i.format('YYYY-MM-DD')


    # Just gets the info and puts it into programmer friendly names
    def getclosing(date, company):
        # Thanks to stackoverflow user 'TessellatingHeckler' for helping me out with this next function! At the time dictionaries were a foreign concept to me.
        readings = company.get_historical(date, date)
        for reading in readings:
            close = reading['Close']
            return close

    company = Share(companyname)
    closingonedayago = getclosing(str(dates[0]), company)
    closingtwodaysago = getclosing(str(dates[1]), company)
    closingthreedaysago = getclosing(str(dates[2]), company)
    closingfivedaysago = getclosing(str(dates[3]), company)
    closingoneweekago = getclosing(str(dates[4]), company)
    twohundredavg = company.get_200day_moving_avg()
    fiftyavg = company.get_50day_moving_avg()
    today = company.get_price()
    decision(today, closingonedayago, closingtwodaysago, closingthreedaysago, closingfivedaysago, closingoneweekago, twohundredavg, fiftyavg)


# All this does is get information, display it in a readable fasion, and then determine based on short term and long term
# data if the stock is worth investing in. It uses a system of points (titled positive and negative), which it ads up
# and uses to determine if the stock is overall 'good' or 'bad'. If you don't understand just look at the code.
def decision(today, oneday, twoday, threeday, fiveday, oneweek, twohundredavg, fiftyavg):
    # The 'negative' and 'positive' values will act like a score, and in the end will be used to determine an 'overall' score of good or bad.
    negative = 0
    positive = 0
    print "Today's price: " + str(today)
    print "Yesterday's price: " + str(oneday)
    print "Two days ago's price: " + str(twoday)
    print "Three days ago's price: " + str(threeday)
    print "Five days ago's price: " + str(fiveday)
    print "One week ago's price: " + str(oneweek)
    print "Fifty day moving average: " + str(fiftyavg)
    print "Two hundred day moving average: " + str(twohundredavg)
    print ""

    # These are just for doing short term stuff. Longer term stuff (50 and 200 day moving averages) comes 20 lines later
    prices = filter(None, [oneweek, fiveday, threeday])
    recentprices = filter(None, [twoday, oneday, today])

    pricenumber = 0
    recentpricenumber = 0

    for i in prices:
        pricenumber += float(i)

    for i in recentprices:
        recentpricenumber += float(i)

    # pricenumber is just the average of oneweek, fiveday, and threeday.
    # recentpricenumber is the average of twoday, oneday, and today.
    # These variables give a pretty good average for different time periods.
    pricenumber = pricenumber / len(prices)
    recentpricenumber = recentpricenumber / len(recentprices)

    if recentpricenumber > pricenumber:
        print "In the past week, the stock has been moving upwards in price."
        positive += 1
    else:
        print "In the past week, the stock has been decreasing in price."
        negative += 1

    # Now these are the longer term things
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
        if negative == 3:
            print "This stock looks like it is doing VERY poor! I wouldn't invest in it."
            end()
        if negative - positive == 1:
            print "This stock is doing pretty bad. It might recover in the near future, but for now I wouldn't buy it."
            end()
        print "This stock looks like it isn't doing well... I wouldn't invest in it."
        end()
    elif negative < positive:
        if positive == 3:
            print "This stock looks like it is doing very well right now! I would invest in it!"
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

# Stock_advisor
Written in python 2.7, this program uses the Yahoo_finance api for python to get stock-related info about a company the user inputs, and then looks at how the company's stock has been doing to give the user advice on whether they should buy some of that company or not.
This program requires the following modules:
yahoo_finance (https://pypi.python.org/pypi/yahoo-finance/1.2.1)
arrow (https://pypi.python.org/pypi/arrow)
datetime (included with python)

The input/output is pretty self explanatory:
-------------------------------
Enter the abbreviation of the company you'd like to look into, for example, 'Google' would be 'GOOGL'
Company Abbreviation: GOOGL
Thank you, please wait a minute while the data for your company is being retrieved...
This morning, it opened for $560.01, and right now is at $571.73.
Since this morning, the price has risen by $11.72

Would you like some info about what the stock has been like in the past few days? Yes/No: yes
Okay, please wait a moment
Analyzing data from the past few days...
Today's price: 571.73
Yesterday's price: None
Two days ago's price: None
Three days ago's price: 556.109985
Five days ago's price: 541.700012
One week ago's price: 545.619995
Fifty day moving average: 550.05
Two hundred day moving average: 545.31

In the past week, the stock has been moving upwards in price.
The fifty day average is greater than the two hundred day average, which signifies a longer term upwards trend.
This stock looks like it is doing very well right now! I would invest in it!

Alright, goodbye!
Press the 'return' or 'enter' key to exit...
-------------------------------
The 'Yesterday's price' and 'Two days ago's price' say "None" because I did this on a Monday, and the stock market is closed over the weekend.

Also, by using this program you agree to take full responsibility if you lose any money by following this program's advice. I never said that the advice it gives would be accurate, so don't sue me if you invest all your money in the stocks it recomends and then lose your house.

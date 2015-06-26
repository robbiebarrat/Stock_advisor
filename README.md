# Stock_advisor
This program uses the Yahoo_finance api for python to get basic stock info for a company the user inputs, and then looks at how the company's stock has been doing to give the user advice on whether they should buy some of that company or not.

The input/output is pretty self explanitory:

---------------------------------------------------------------------------------------------------------------------

Enter the abbreviation of the company you'd like to look into, for example, 'Google' would be 'GOOGL'
Company Abbreviation: XRX
Thank you, please wait a minute while the data for your company is being retrieved...
This morning, it opened for $10.960, and right now is at $10.995.
Since this morning, the price has risen by $0.035

Would you like some info about what the stock has been like in the past few days? Yes/No: yes
Okay, please wait a moment
Calculating date stuffs...
Analyzing data from the past few days...
Today's price: 10.995
Yesterday's price: 11.01
Two days ago's price: 10.99
Three days ago's price: 11.25
Fifty day moving average: 11.271
Two hundred day moving average: 12.745


There have been some inconsistencies with the pattern, but today's price is lower than three day's ago.
There is a %1.02319236016 difference between the price three days ago and today's price.
The two hundred day average is greater than the fifty day average, which signifies a longer term downwards trend.
This stock looks like it isn't doing well... I wouldn't invest in it.

Alright, goodbye!
Press the 'return' or 'enter' key to exit...
---------------------------------------------------------------------------------------------------------------------

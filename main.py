#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator")
Total_Bill=float(input('what was your total bill? '))
percentage=int(input('what percentage would you like to tip? 10,12 or 15? '))
split=int(input('how many people to split bill with? '))
tipperperson= round((Total_Bill/split) * (percentage/100 * 1),2)
split_person=Total_Bill/split
Finalamount=tipperperson + split_person
print('Each person should pay with tip:', Finalamount)

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


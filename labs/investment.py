### Check the README for additional information ###
# Fund	1980 CPS (USD)	1996 CPS (USD)	2012 CPS (USD)	2016 CPS (USD)	Current CPS (USD)
# Fund A	$2.50	$3.75	$4.10	$5.10	$6.00
# Fund B	$12.02	$14.10	$15.76	$18.08	$21.01
# Fund C	$8.65	$8.03	$11.15	$19.82	$23.01
# Fund D	$0.63	$1.22	$1.45	$2.01	$1.83

funds = {
    "A": {
        1980: 2.50,
        1996: 3.75,
        2012: 4.10,
        2016: 5.10,
        2023: 6.00
    },
    "B": {
        1980: 12.02,
        1996: 14.10,
        2012: 15.76,
        2016: 18.08,
        2023: 21.01
    },
    "C": {
        1980: 8.65,
        1996: 8.03,
        2012: 11.15,
        2016: 19.82,
        2023: 23.01
    },
    "D": {
        1980: 0.63,
        1996: 1.22,
        2012: 1.45,
        2016: 2.01,
        2023: 1.83
    }
}


# 1. Create a function called number_shares_a() that only accepts an investment amount and returns the number of shares of Fund A which that investment could buy today.
# Then call the function with two different amounts to ensure that it works properly.
def number_shares_a(investment_amount):
    return investment_amount / funds["A"][2023]


# 2. Create a more-general function called number_shares() that takes in an investment amount and a fund. It should return the number of shares of that fund which that investment could buy today.
# Then call the function with different amounts and different funds.
def number_shares(investment_amount, fund):
    return investment_amount / funds[fund][2023]


# 3. Create a more flexible calculator method called history_shares() that takes in an investment amount, fund, and year and returns the number of shares that money could buy in that year.
def history_shares(investment_amount, fund, year):
    return investment_amount / funds[fund][year]

### Advanced Bonus Challenge ###

# 4. What is the change of an investment over time? Create a method calculate_profit() that accepts an initial investment amount, the fund, and the initial investment year, and returns the current profit made on the initial investment. This is an open ended one - there are many ways to do this!
def calculate_profit(investment_amount, fund, year):
    return "$" + str(round(investment_amount * funds[fund][2023] - investment_amount * funds[fund][year], 2))

# Bonus: Format the output of the function as USD currency, so instead of 1000, the function should output $1000.00.
# print(calculate_profit(1000, "A", 1980))

### Double Advanced Bonus Challenge ###

# 5. Which investment is the best? Create a method best_choice() that accepts an investment amount and a year, and returns the name of the fund that would have made the most money for the investor.
def best_choice(investment_amount, year):
    best_fund = ""
    best_profit = 0
    for fund in funds:
        profit = investment_amount * funds[fund][2023] - investment_amount * funds[fund][year]
        if profit > best_profit:
            best_profit = profit
            best_fund = fund
    return best_fund, best_profit

# Bonus: In addition to the name of the fund, also return how much money the investor would have earned.

### Triple Advanced Bonus Challenge ###

# 6. Consider the current profit difference between making an investment in a fund several years apart. Create a method investment_diff() that accepts an investment amount, a fund, and two year values and returns the current profit difference if the money had been made earlier vs. later.
def investment_diff(investment_amount, fund, year1, year2):
    if year1 > year2:
        return round(investment_amount * funds[fund][year1] - investment_amount * funds[fund][year2], 2)

    return round(investment_amount * funds[fund][year2] - investment_amount * funds[fund][year1], 2)

# Bonus: How can you account for a sloppy investment advisor who puts the years in a different order than you expect?
# print(investment_diff(1000, "A", 1980, 2023))
# print(investment_diff(1000, "A", 2023, 1980))
# Define your functions here

# Here's a function that's already been defined, but it's just a skeleton. It takes one argument (total) that we will
# pass to the function as an integer when we call it. 1. Replace "return" with code such that this function RETURNS
# the message "WARNING: Budget exceeded" if the total is over 100 dollars.

def simple_budget_checker(total):
    return total > 100 and "WARNING: Budget exceeded" or None


# 2. Define a function called budget_checker that checks to make sure the total is less than 100 dollars.
#    If the total is over 100 dollars, return the message "WARNING: Budget exceeded"
#    If the total is under 100 dollars, return the message "You're under budget!"
def budget_checker(total):
    return total > 100 and "WARNING: Budget exceeded" or "You're under budget!"


# 3. Define a function called precise_budget_checker that checks to make sure the total is less than 100 dollars. It
# should do exactly what the budget checker does, but it should ALSO return the message "STOP! Maximum reached" if
# the total is EXACTLY 100 dollars
def precise_budget_checker(total):
    if total > 100:
        return "WARNING: Budget exceeded"
    elif total == 100:
        return "STOP! Maximum reached"
    return "You're under budget!"


# 4. Write a function called ultimate_budget_checker that checks to make sure the total is less than 100 dollars.
#    If the total is under that amount, let the user know how many dollars they have left to spend.
#    If the total is over that amount, let the user know how many dollars worth of items they need to put back.

def ultimate_budget_checker(total):
    if total > 100:
        return "You need to put back " + str(total - 100) + " dollars worth of items."
    return "You have " + str(100 - total) + " dollars left to spend."


# 5. Below is a function called flexible_budget_checker. It hasn't been fully defined yet, but you can see it takes
# two arguments. It should be exactly like the ultimate_budget_checker, except it will check your total against a
# budget YOU enter into the function. For example, the code flexible_budget_checker(40, 50) should return the message
# "WARNING: budget exceeded by 10 dollars."

def flexible_budget_checker(budget, total):
    if total > budget:
        return "WARNING: budget exceeded by " + str(total - budget) + " dollars."
    return "You have " + str(budget - total) + " dollars left to spend."


# 6. CHALLENGE: The trouble with the first four functions is that they only work for a budget of 100 dollars. The
# trouble with the fifth function is that it makes the test provide the budget every time. The best solution to this
# would be to have a global variable called budget before you start defining functions, and then use that variable in
# place of the number 100. GOAL: Refactor (rewrite) the first four functions, but change the literal 100 to a global
# variable. Then test out the functions to see if they still work if the budget (stored in the global variable) is
# cut down to 40 dollars.
budget = 40


def final_budget_checker(total):
    if total > budget:
        return "WARNING: budget exceeded by " + str(total - budget) + " dollars."
    return "You have " + str(budget - total) + " dollars left to spend."

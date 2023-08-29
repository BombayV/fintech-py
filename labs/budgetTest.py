import budget # This first line imports the file called budget.py, and the function you're creating called simple_budget_checker() and all the others will be stored within that file.

# In this file you will be testing the different budget checker functions you wrote in the budget.py file.
# Remember that since your functions will be RETURNING information, it will only be visible if you PRINT that return value out to the console.
# Also, because the functions are in a different file, you must access them using dot syntax like "budget.simple_budget_checker()" to let the
#     computer know where to find their definitions.

# Here are tests for the first three functions you wrote. Uncomment them to see them in action.
# Notice that they test both pass and fail cases, to make sure the functions work for any input.

print(budget.simple_budget_checker(75)) # This test should print "None", to represent null or no value, because 75 is less than 100 dollars, and we haven't yet set a condition to handle this case.
print(budget.simple_budget_checker(120)) # This test should print a warning because 120 is more than 100 dollars.

print(budget.budget_checker(132)) # This test should print a warning because the budget has been exceeded.
print(budget.budget_checker(69)) # This test should print a message saying that the user is under budget.

print(budget.precise_budget_checker(100)) # This test should alert the user that they are at their maximum budget.
print(budget.precise_budget_checker(132)) # This test should print a warning because the budget has been exceeded.
print(budget.precise_budget_checker(69)) # This test should print a message saying that the user is under budget.




# Here you should try writing your own tests for ultimate_budget_checker().
# Make sure that you test each possible outcome so you know the function is working for any input, not just a success case.




# Once again, write your own tests for flexible_budget_checker().
# Try testing it with different budgets and different totals to make sure it always returns the correct result.

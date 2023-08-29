### Code Along - Loops ###

# # Earlier, you learned how to make Python say "hello" - now let's write some print statements to get it to say one
# "hello" for each person in the class.  Go!


# #I. LOOPING OVER RANGES - Here's the most basic type of for loop. What do you think will happen when we run these
# examples?

# for i in range(15):
#   print("Hello")


# for i in range(5,8):
#   print("Hello")


# for i in range(0,8):
#   print("Hello")


# #II. THE CONSTANT OF ITERATION - We're using the placeholder i to keep track of our count. If we wanted to count
# more visibly (instead of behind the scenes), we could do something like this:

# for i in range(10):
#   print(f"i is currently: {i}")
#   print("Hello")



# # Try this - what happens if we change the term 'i' to be some other variable?  Does it change anything about how
# the code works?


# #III. LOOPING ALGORITHMS -- There are a ton of really cool ways to use this new superpower we've acquired. Here's
# one.  Imagine you wanted to sum the numbers 5, 6, 7, and 8. Here's how you can do it using a for loop:

# sum = 0
# for i in range(5,9):
#   sum += i
#   print(f"The sum is currently {sum}.")

# print(f"The loop is over, and the total is {sum}!")


# #Try it - can you get python to sum up the numbers 1 through 20? Hint - see if you can get your loop to print out
# some progress along the way so that you can tell if it's working properly. #What about multiplying the numbers 1 to
# 100? Can you imagine some ways this would be


##IV. LOOPING WITH A CONDITION -- You may also find it useful to combine loops with conditionals. Here's an example:

# print("Type a secret number here, and I'll try to guess it.")
# secret_number = int(input("Pick a single digit number please!"))

# for i in range(10): # remember this goes from 0 to 10, excluding 10
#   if i < secret_number:
#     print(f"Looks like it's not {i}, so I'll keep guessing...")
#   elif i == secret_number:
#     print(f"OH! Your number is {i}!")


##V. LOOPING OVER STRINGS

# #One of the most useful features of Python is how simply it can break one piece of information (like a String) into
# its component parts (letters/characters).  What do you think this will print?

# print("hello"[2])


# Let's say we wanted to use for loops to spell out the word "hello" one letter at a time.  How could we do it?


# #This opens up some cool possibilities for us.  Take a look at the following two examples.  Can you figure out what
# they're doing and how they're working?

# your_word = input("Give me a word and I'll spell it.")

# print(f"Okay! I'll try to spell {your_word}.")
# for letter in your_word:
#   print(letter)


####This code will count the number of "j"s in a phrase.  Take a look:
# number_of_appearances = 0

# for letter in "jumping jolly jackrabbits!":
#   if letter == "j":
#     number_of_appearances += 1

# print(f"Looks like the letter j showed up {number_of_appearances} times.")

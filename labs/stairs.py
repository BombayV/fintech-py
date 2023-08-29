def upstairs(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '#' * (i + 1))

def downstairs(n):
    for i in range(n):
        print('#' * (i +1))

# Print a pyramid of height n and a space in the middle
   # #
  ## ##
 ### ###
#### ####
def pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '#' * (i + 1) + ' ' + '#' * (i + 1))

# _    _                  _         ______         _  _
# | |  | |                | |        |  _  \       | || |
# | |  | |  ___   _ __  __| | ______ | | | | _   _ | || |
# | |/\| | / _ \ | '__|/ _` ||______|| | | || | | || || |
# \  /\  /| (_) || |  | (_| |        | |/ / | |_| || || |
# \/  \/  \___/ |_|   \__,_|        |___/   \__,_||_||_|
# print the word Word-Dull in ascii art

def word_dull():
    print(' _    _                  _         ______         _  _')
    print('| |  | |                | |        |  _  \       | || |')
    print('| |  | |  ___   _ __  __| | ______ | | | | _   _ | || |')
    print("| |/\| | / _ \ | '__|/ _` ||______|| | | || | | || || |")
    print('\  /\  /| (_) || |  | (_| |        | |/ / | |_| || || |')
    print(' \/  \/  \___/ |_|   \__,_|        |___/   \__,_||_||_|')
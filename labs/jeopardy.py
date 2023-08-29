import requests
import random
from similar_text import similar_text

response = requests.get('http://jservice.io/api/clues').json()


# print(response)

# LEVEL 1
# Print out just the first item in the entire response.
# print(response[0])

# Print out just the question of the first item in the entire response.
# print(response[0]["question"])
#
# You might notice that each of the dictionary keys has the letter u in front of it - this just means the string that follows is represented in Unicode, and it won't affect your code in any way today. You can igore the u.
#
# Refactor your code so that it prints out a random question, not just the first one every time.
# random_question = random.choice(response)
# print(random_question["question"])

#
# Now, get some user input after the question. If what they type matches the answer, print a "congratulations!" message of some sort. If it doesn't match, print a "sorry" message of some sort.
#
# answer = input("Your answer:\n")
# if answer == random_question["answer"]:
#     print("Congratulations!")
# else:
#     print("Sorry")

# It's important to think about how specific Python's matching will be. If the user types "gorge" but the correct answer is "Gorge.", then the user will get the question wrong. Consider finding a way of making your program responsive to small variations in capitalization or punctuation.
# If you get it wrong, you probably still want to know the right answer - it can be so frustrating if you were sure you were right. If the user gets it wrong, print out a message that tells them what the correct answer really was.
#

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# LEVEL 2
# Wrap this game in a loop so the user can play multiple rounds.
# score = 0
# while True:
#     random_question = random.choice(response)
#     random_answer = random_question["answer"].lower()
#     print(f"{bcolors.OKCYAN}Question: {bcolors.ENDC}{random_question['question']}")
#     answer = input(
#         f"{bcolors.OKCYAN}Debug: {bcolors.ENDC}{random_answer}\n{bcolors.OKCYAN}Your answer: {bcolors.ENDC}{bcolors.BOLD}")
#     # if the answer is close enough to the real answer, then let them know they almost had it
#     while similar_text(answer, random_answer) > 50 and answer != random_answer:
#         answer = input(
#             f"{bcolors.ENDC}\n{bcolors.WARNING}Try again, you're close.\n{bcolors.OKCYAN}Your answer: {bcolors.ENDC}{bcolors.BOLD}").lower()
#
#     if answer == random_answer:
#         print(f"{bcolors.ENDC}{bcolors.OKGREEN}Congratulations!")
#         score += random_question["value"] or 0
#     else:
#         print(f"{bcolors.ENDC}{bcolors.FAIL}Sorry. The correct answer was " + random_answer)
#         score -= random_question["value"] or 0
#
#     playAgain = input(
#         f"{bcolors.OKCYAN}Score: {bcolors.ENDC}${score}\n{bcolors.OKCYAN}Play again? {bcolors.ENDC}(y/n)\n\n")
#     if playAgain == "n":
#         break

#
# Create a score variable:
#
# If the user gets a question right, increase their score by the point value of the question. If the user gets a
# question wrong, decrease their score by the point value of the question. Print out their score after each round.
# LEVEL 3 One of the most frustrating parts of this game is missing an answer due to typos, spelling errors,
# capitalization mismatches, or unexpected punctuation. Some of this is relatively easy to fix with Python's core
# methods, but there is no core function to show that "george" and "gorge" are SO CLOSE that the user probably
# actually knew the answer. There's a library called similar-text that will let us examine how similar two strings
# are. Remember that you'll need to install it, just like we did for requests. You'll want to look it up,
# but it might look something like pip3 install similar_text Install that library, import it at the top of your
# program, and then look at the documentation to figure out how to use it. If the user's answer is really close to
# the real answer, let them know that they almost have it, but that they may want to type it more carefully. It may
# also be beneficial to consider a way of recognizing that "Grapes of Wrath" and "The Grapes of Wrath" would be
# considered a mismatch. Are you going to give the user another chance if all they're missing is a small word like
# "the"? Jeopardy Board
#
# LEVEL 4 The real jeopardy board has six categories, and 5 questions per category of increasing difficulty. That's
# 30 unique questions. The player also gets to CHOOSE which questions to answer and when. Find a way to load all 30
# questions, and then offer the user a choice of which question to attempt. Find a way to print out a visual
# representation of the board in the console. Bonus: print the score at the top or bottom of the board. Keep track of
# which questions the user has already tried, and throw them an error if they try to access the same question twice.

board = []
score = 0

for i in range(6):
    board.append([])
    for j in range(5):
        board[i].append({
            "question": response[i + j]["question"],
            "answer": response[i + j]["answer"],
            "value": j * 100 + 100,
            "answered": False,
            "id": f"{chr(i + 65)}{j + 1}"
        })


def find_question(questionId):
    for x in range(6):
        for y in range(5):
            if board[x][y]["id"] == questionId:
                return board[x][y]
    return None


def print_board(start=False):
    if start:
        print(f"{bcolors.HEADER}Welcome to Jeopardy!\n{bcolors.ENDC}Here is the board:\n")

    print(f"{bcolors.WARNING}Category 1\tCategory 2\tCategory 3\tCategory 4\tCategory 5\tCategory 6{bcolors.ENDC}")
    for x in range(5):
        for y in range(6):
            if board[y][x]["answered"]:
                print(f"{bcolors.FAIL}Answered\t{bcolors.ENDC}", end="")
            else:
                print(f"{bcolors.OKGREEN}{board[y][x]['value']}\t\t{bcolors.ENDC}", end="")
        print("\n")
    print(f"{bcolors.OKCYAN}Score: {bcolors.ENDC}${score}\n")


print_board(True)

userQuestion = input(
    f"{bcolors.OKCYAN}Which question would you like to answer? {bcolors.ENDC}(ex. A1 | exit)\n").upper()
if userQuestion == "EXIT":
    exit()

while find_question(userQuestion) is None or find_question(userQuestion)["answered"]:
    userQuestion = input(f"{bcolors.FAIL}Invalid question. Try again.{bcolors.ENDC}\n").upper()

while True:
    question = find_question(userQuestion)
    print(f"{bcolors.OKCYAN}Question: {bcolors.ENDC}{question['question']}")
    answer = input(
        f"{bcolors.OKCYAN}Debug: {bcolors.ENDC}{question['answer']}\n{bcolors.OKCYAN}Your answer: {bcolors.ENDC}{bcolors.BOLD}").lower()
    # if the answer is close enough to the real answer, then let them know they almost had it
    while similar_text(answer, question["answer"].lower()) > 50 and answer != question["answer"].lower():
        answer = input(
            f"{bcolors.ENDC}\n{bcolors.WARNING}Try again, you're close.\n{bcolors.OKCYAN}Your answer: {bcolors.ENDC}{bcolors.BOLD}").lower()

    if answer == question["answer"].lower():
        print(f"{bcolors.ENDC}{bcolors.OKGREEN}Congratulations!")
        score += question["value"] or 0
    else:
        print(f"{bcolors.ENDC}{bcolors.FAIL}Sorry. The correct answer was " + question["answer"].lower())
        score -= question["value"] or 0

    question["answered"] = True
    print_board()
    userQuestion = input(
        f"{bcolors.OKCYAN}Which question would you like to answer? (ex. A1 | exit){bcolors.ENDC}\n").upper()
    if userQuestion == "EXIT":
        break

    while find_question(userQuestion) is None or find_question(userQuestion)["answered"]:
        userQuestion = input(f"{bcolors.FAIL}Invalid question. Try again.{bcolors.ENDC}\n").upper()

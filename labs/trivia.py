import requests
import random

url = "https://opentdb.com/api.php?amount=10"
response = requests.get(url).json()
if response["response_code"] != 0:
    print("Error fetching questions" + response.response_code)

questions = response["results"]
score = 0


def randomize_answers(q):
    answers = q["incorrect_answers"]
    answers.append(q["correct_answer"])
    random.shuffle(answers)
    return answers


for question in questions:
    print(question["question"])
    ran_answers = randomize_answers(question)
    for i, answer in enumerate(ran_answers):
        print(str(i + 1) + ". " + answer)

    user_answer = input("Enter your answer: ").lower()
    if user_answer == question["correct_answer"].lower() or user_answer == str(
            ran_answers.index(question["correct_answer"]) + 1):
        score += 1

print("Your score is " + str(score) + "/10")

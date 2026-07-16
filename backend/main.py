import database
import pyfiglet
import random


# Printing UI
text = pyfiglet.figlet_format("Crack", font = "standard", width = 200)
text1 = pyfiglet.figlet_format("AI Interview Coach", font = "standard", width = 100)

print('==========================================================================================')
print(text.rstrip())
print(text1.rstrip())
print('==========================================================================================')

# Asking for roles, no. of questions and difficulty
user_role = input("Role: ")
selected_difficulty = input("Difficulty: ")
number_of_questions = int(input("Number of Questions: "))

# Role and topics
role_folder = user_role.replace(" ", "_").lower()

# Accessing the Data
questions = database.load_questions(role_folder)

# Filtering questions by difficulty 
filtered_questions = []

for question in questions:
    if question["difficulty"] == selected_difficulty:
        filtered_questions.append(question)

# Error handling
if number_of_questions > len(filtered_questions):
    print("Not enough questions available")
    exit()

# How many Questions?
selected_questions = random.sample(filtered_questions, number_of_questions)

# Storing answers
answers = []

# Printing questions

for index, question in enumerate(selected_questions, start = 1):

    print('=' * 40)
    print(f"Question {index}/{number_of_questions}")
    print('=' * 40)

    print(question["question"])
    print()

    print("Difficulty:", question["difficulty"].title())
    print()
    
    answer = input("Answer: ")
    print()
    answers.append(answer)

print("Interview Complete!")
print(f"Questions Answered: {number_of_questions}")





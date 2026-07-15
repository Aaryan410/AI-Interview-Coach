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

# Asking for roles, topics and no. of questions
user_role = input("Role: ")
user_topic = input("Topic: ")
number_of_questions = int(input("Number of Questions: "))

# Role and topics
role_folder = user_role.replace(" ", "_").lower()
topic_file = user_topic.replace(" ", "_").lower()

# Accessing the Data
questions_data = database.load_questions(role_folder, topic_file)

# Accessing the list inside the data
questions_list = questions_data[topic_file]

# Question
selected_questions = random.sample(questions_list, number_of_questions)

# Storing answers
answers = []

# Printing questions

for question in selected_questions:
    print('---------------------------------------')
    print()
    print(question["question"])
    print()
    print(question["difficulty"].title())
    print()
    print('---------------------------------------')
    print('---------------------------------------')
    print()
    answer = input("Answer: ")
    print()
    answers.append(answer)

print("Interview Complete!")
print(f"Questions Answered: {number_of_questions}")





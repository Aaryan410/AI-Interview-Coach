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

# Asking for roles and topics
user_role = input("Role: ")
user_topic = input("Topic: ")

# Role and topics
role_folder = user_role.replace(" ", "_").lower()
topic_file = user_topic.replace(" ", "_").lower()

# Accessing the Data
questions_data = database.load_questions(role_folder, topic_file)

# Accessing the list inside the data
questions_list = questions_data[topic_file]

# Question
random_question_obj = random.choice(questions_list)


# Printing questions

print('---------------------------------------')
print()
print(random_question_obj)
print()
print('---------------------------------------')
print()
print(random_question_obj["question"])
print()
print(random_question_obj["difficulty"])
print()
print('---------------------------------------')
print()

answer = input("Answer: ")



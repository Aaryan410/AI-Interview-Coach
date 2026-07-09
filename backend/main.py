import interview
import pyfiglet
import random

# Printing UI
text = pyfiglet.figlet_format("AI Interview Coach", font = "standard", width = 200)

print('==========================================================================================')
print(text.rstrip())
print('==========================================================================================')

# Asking for roles
user_role = input("Role: ")

# Role
role = user_role.replace(" ", "_").lower()

# Accessing the Data
questions = interview.load_questions(role)

# Questions
selected_category = random.choice(list(questions.keys()))

# Category
selected_question = random.choice(questions[selected_category])


# Printing questions
print()
print(f"Category: {selected_category.title()}")
print()
print(f"Difficulty: {selected_question["difficulty"].title()}")
print()
print(f"Question ID: {selected_question["id"]}")
print()
print('---------------------------------------')
print()

answer = input("Answer: ")



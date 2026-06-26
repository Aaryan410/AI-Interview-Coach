import interview
import pyfiglet

roles = {
    "1": "software_engineer",
    "2": "data_scientist",
    "3": "devops_engineer"
}

# Printing UI
text = pyfiglet.figlet_format("AI Interview Coach", font = "standard", width = 200)

print('==========================================================================================')
print(text.rstrip())
print('==========================================================================================')

print()
print()

print("Roles:")
print("1. Software Engineer")
print("2. Data Scientist")
print("3. DevOps Engineer")

print()

role = input("> ")
role = roles[role]

# Accessing the Data
questions = interview.load_questions(role)

# Printing questions
print()
print(questions["Software Engineer"]["programming fundamentals"][0]["question"])

# AI Interview Coach - Project Progress

## Sprint 1 (Day 1)

### ✅ Completed
- Created GitHub repository
- Set up virtual environment
- Created project structure
- Added interview questions database (`questions.json`)
- Implemented `load_questions(filename)` using `with open()` and `json.load()`
- Connected `main.py` with `interview.py`
- Successfully loaded and printed the question database

### 📚 Concepts Learned
- Function parameters
- Return values
- JSON files
- Python modules
- Importing functions
- Context managers (`with open()`)

### 📝 Next Sprint
- Display available interview roles
- User selects a role
- Display the first interview question

### 🐛 Bugs Solved
- Misused `requests.get()` for local files
- Confused `json.load()` and `json.dumps()`
- Learned the difference between importing a module and using its functions
- Learned why `__pycache__` is created
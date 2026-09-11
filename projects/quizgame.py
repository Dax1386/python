questions = (
    "What is the output of type(3.14) in Python?",
    "Which keyword is used to define a function in Python?",
    'Given fruits = ["apple", "banana", "cherry"], what does fruits[0] return?',
    "Which symbol is used for single-line comments in Python?",
    "What is the result of the floor division operation 10 // 3?",
)

options = (("A. <class 'int'>", "B. <class 'float'>", "C. <class 'str'>", "D. <class 'bool'>"),
              ("A. func", "B. def", "C. function", "D. define"),
              ("A. apple", "B. banana", "C. cherry", "D. None"),
              ("A. //", "B. #", "C. /* */", "D. <!-- -->"),
              ("A. 3", "B. 3.0", "C. 4", "D. 3.33"))

answers = ("B", "B", "A", "B", "A")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("-------------------------------------------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
    questions_num += 1

print()

print(f"all correct answer is:{answers}" , end=", ")
print(f"your guesses are:{guesses}" , end=", ")

print()

print("RESULT")
score = int((score / len(questions)) * 100)
print(f"Your score is: {score}%")



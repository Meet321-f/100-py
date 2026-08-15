questions = [
    {
        "question": "Which language are we learing?",
        "options": ["Python", "Java", "C++", "JavaScript"],
        "answer": "Python"
    },
    {
        "question" : "Which keyword is used to define a function in Python?",
        "options": ["def", "function", "func", "define"],
        "answer": "def"
    },
    {
        "question" : "Which symbol is used for comments in Python?",
        "options": ["#", "//", "/* */", "<!-- -->"],
        "answer": "#"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for i, option in enumerate(q["options"], start=1):
        print(f"{i}.{option}")

    answer = int(input("Enter the number of your answer: "))
    # print()

    

    if answer == 1:
        selected_option = q["options"][0]
    elif answer == 2:
        selected_option = q["options"][1]
    elif answer == 3:
        selected_option = q["options"][2]
    elif answer == 4:
        selected_option = q["options"][3]
    else:
        selected_option = ""

    if selected_option == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"Your current score is: {score}/{len(questions)}")

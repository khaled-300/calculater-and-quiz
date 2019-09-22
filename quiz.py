from Question import Question


question_prompts = [
    "what  color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what  color are Bananas?\n(a) Teal\n(b) magenta\n(c) yellow\n\n",
    "what  color are strawberries?\n(a) Red\n(b) blue\n(c) yellow\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")

]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)
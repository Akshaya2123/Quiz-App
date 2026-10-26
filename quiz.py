

QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "function",
            "B": "def",
            "C": "define",
            "D": "fun",
        },
        "answer": "B",
    },
    {
        "question": "Which data type is used to store key-value pairs in Python?",
        "options": {
            "A": "List",
            "B": "Tuple",
            "C": "Dictionary",
            "D": "Set",
        },
        "answer": "C",
    },
    {
        "question": "Which symbol is used for single-line comments in Python?",
        "options": {
            "A": "//",
            "B": "<!--",
            "C": "#",
            "D": "/* */",
        },
        "answer": "C",
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": {
            "A": "input()",
            "B": "display()",
            "C": "echo()",
            "D": "print()",
        },
        "answer": "D",
    },
    {
        "question": "Which loop is commonly used to iterate over a sequence?",
        "options": {
            "A": "for",
            "B": "repeat",
            "C": "iterate",
            "D": "foreach",
        },
        "answer": "A",
    },
]


def display_instructions():
    
    print("\n========== QUIZ INSTRUCTIONS ==========")
    print("1. The quiz contains multiple-choice questions.")
    print("2. Each question has four options: A, B, C, and D.")
    print("3. Enter the letter of the option you choose.")
    print("4. You can enter answers in uppercase or lowercase.")
    print("5. Each correct answer earns 1 point.")
    print("6. Incorrect answers earn 0 points.")
    print("7. Your final score and percentage are shown at the end.")
    print("=======================================\n")


def get_valid_choice(prompt, valid_choices):
   
    while True:
        try:
            choice = input(prompt).strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Returning to the menu.")
            return None

        if choice in valid_choices:
            return choice

        print(f"Invalid choice. Please enter one of: {', '.join(valid_choices)}.")


def run_quiz():
   
    correct_answers = 0
    incorrect_answers = 0
    total_questions = len(QUESTIONS)

    print("\nWelcome to the Python Quiz!")
    print("Answer each question by entering A, B, C, or D.\n")

    for number, item in enumerate(QUESTIONS, start=1):
        print(f"Question {number}: {item['question']}")

        for letter, option_text in item["options"].items():
            print(f"{letter}. {option_text}")

        answer = get_valid_choice("Enter your answer: ", ["A", "B", "C", "D"])
        if answer is None:
            print("Quiz cancelled.")
            return

        if answer == item["answer"]:
            correct_answers += 1
            print("Correct answer!\n")
        else:
            incorrect_answers += 1
            correct_letter = item["answer"]
            correct_text = item["options"][correct_letter]
            print(f"Incorrect. Correct answer: {correct_letter}. {correct_text}\n")

    percentage = (correct_answers / total_questions) * 100 if total_questions else 0

    print("========== QUIZ RESULTS ==========")
    print(f"Total Questions : {total_questions}")
    print(f"Correct Answers : {correct_answers}")
    print(f"Incorrect Answers: {incorrect_answers}")
    print(f"Final Score     : {correct_answers}/{total_questions}")
    print(f"Final Percentage: {percentage:.0f}%")

    if percentage == 100:
        feedback = "Excellent! Perfect score!"
    elif percentage >= 80:
        feedback = "Very good job!"
    elif percentage >= 60:
        feedback = "Good job! Keep practising."
    elif percentage >= 40:
        feedback = "Nice effort. Review the topics and try again."
    else:
        feedback = "Keep learning and try again. You can improve!"

    print(f"Performance     : {feedback}")
    print("==================================\n")


def main():
   
    while True:
        print("====== QUIZ APPLICATION ======")
        print("1. Start Quiz")
        print("2. View Quiz Instructions")
        print("3. Exit")
        print("==============================")

        choice = get_valid_choice("Enter your choice (1-3): ", ["1", "2", "3"])

        if choice is None:
            print("Thank you for using the Quiz Application!")
            break
        elif choice == "1":
            run_quiz()
            if get_valid_choice("Would you like to play again? (yes/no): ", ["YES", "NO"]) == "YES":
                continue
            print("Thank you for playing!")
            break
        elif choice == "2":
            display_instructions()
        elif choice == "3":
            print("Thank you for using the Quiz Application. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuiz application closed. Goodbye!")

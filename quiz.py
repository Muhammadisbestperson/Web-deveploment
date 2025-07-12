def run_quiz():
    questions = [
        {
            "question": "Who is the first pm of Pakistan ?",
            "options": ["A. Imran Khan", "B. Liaquat Ali", "C. Benazir Bhutto", "D.Narendra Modi "],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Largest Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "C"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        }
    ]

    score = 0
    print("Welcome to the Python Quiz!")

    for q_data in questions:
        print(f"\n{q_data['question']}")
        for option in q_data['options']:
            print(option)

        user_answer = input("Enter your answer (A, B, C, or D): ").upper()

        if user_answer == q_data['answer']:
            print("Correct!")
            score += 10
        else:
            print(f"Incorrect. The correct answer was {q_data['answer']}.")

    print(f"\nQuiz finished! You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()

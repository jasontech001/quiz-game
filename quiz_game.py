print("🧠 Welcome to the Quiz Game!\n")

questions = [
    {"question": "What is the capital of Nigeria?", "answer": "Abuja"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "What programming language are we using?", "answer": "Python"},
    {"question": "What year are we in?", "answer": "2025"},
    {"question": "How many days are in a leap year?", "answer": "366"}
]

score = 0

for i, q in enumerate(questions):
    user_answer = input(f"Q{i+1}: {q['question']} \n> Your Answer: ")
    if user_answer.strip().lower() == q["answer"].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer is: {q['answer']}\n")

print(f"🎉 Game Over! Your final score: {score}/{len(questions)}")

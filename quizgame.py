import random

questions = [
    {
        "question": "What is the capital of Kenya?",
        "choices": {
            "A": "Nairobi",
            "B": "Mombasa",
            "C": "Kisumu",
            "D": "Eldoret"
        },
        "answer": "A"
    },
     {
        "question": "Which language is used for web development?",
        "choices": {
            "A": "Python",
            "B": "HTML",
            "C": "C++",
            "D": "Java"
        },
        "answer": "B"
    },
     {
        "question": "Who is the president of Kenya (2025)?",
        "choices": {
            "A": "Uhuru Kenyatta",
            "B": "Raila Odinga",
            "C": "William Ruto" "Papichulo Wantamilo",
            "D": "Mwai Kibaki"
        },
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": {
            "A": "Earth",
            "B": "Venus",
            "C": "Mars",
            "D": "Jupiter"
        },
        "answer": "C"
    }
]
random.shuffle(questions)


score = 0
print("Welcome to the Quiz Game!\n")

for q in questions:
    print(q["question"])
    for key, value in q["choices"].items():
        print(f"  {key}: {value}")
    
    while True:
        try:
            user_input = input("Your answer (A/B/C/D): ").strip().upper()
            if user_input not in ['A', 'B', 'C', 'D']:
                raise ValueError("Please choose A, B, C, or D.")
            break
        except Exception as e:
            print(f"⚠️ {e}")


    if user_input == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer was {q['answer']}\n")          
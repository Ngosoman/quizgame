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
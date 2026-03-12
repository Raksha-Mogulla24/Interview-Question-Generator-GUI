# interview_question_generator_gui.py

import tkinter as tk
from tkinter import ttk
import random

questions = {
    "python": {
        "Easy": [
            "What is Python?",
            "What are Python lists?",
            "What is a variable in Python?",
            "What is indentation in Python?"
        ],
        "Medium": [
            "Explain list vs tuple.",
            "What is a dictionary in Python?",
            "What are Python modules?",
            "What is exception handling?"
        ],
        "Hard": [
            "Explain Python decorators.",
            "What are generators in Python?",
            "Explain multithreading in Python.",
            "Explain Python memory management."
        ]
    },

    "java": {
        "Easy": [
            "What is Java?",
            "What is JVM?",
            "What is a class in Java?"
        ],
        "Medium": [
            "Explain OOP concepts in Java.",
            "Difference between ArrayList and LinkedList?",
            "What is inheritance?"
        ],
        "Hard": [
            "Explain Java memory management.",
            "What is multithreading in Java?",
            "Explain synchronization."
        ]
    },

    "data structures": {
        "Easy": [
            "What is a stack?",
            "What is a queue?",
            "What is an array?"
        ],
        "Medium": [
            "What is a linked list?",
            "Explain binary tree.",
            "What is a hash table?"
        ],
        "Hard": [
            "Explain AVL trees.",
            "What is a Red-Black tree?",
            "Explain graph traversal algorithms."
        ]
    }
}

def generate_questions(count):

    topic = topic_combo.get().lower()
    difficulty = difficulty_combo.get()

    result_box.delete(1.0, tk.END)

    if topic not in questions:
        result_box.insert(tk.END,"Invalid topic")
        return

    question_list = questions[topic][difficulty]

    generated = []

    for i in range(count):
        q = random.choice(question_list)
        generated.append(q)

    result = "Generated Questions:\n\n"

    for i,q in enumerate(generated,1):
        result += f"{i}. {q}\n"

    result_box.insert(tk.END,result)

    with open("generated_questions.txt","w") as f:
        f.write(result)


# GUI
window = tk.Tk()
window.title("Interview Question Generator")
window.geometry("550x450")

title = tk.Label(window,text="Interview Question Generator",font=("Arial",16))
title.pack(pady=10)

# Topic
topic_label = tk.Label(window,text="Select Topic:")
topic_label.pack()

topic_combo = ttk.Combobox(window)
topic_combo["values"] = ["Python","Java","Data Structures"]
topic_combo.current(0)
topic_combo.pack(pady=5)

# Difficulty
difficulty_label = tk.Label(window,text="Select Difficulty:")
difficulty_label.pack()

difficulty_combo = ttk.Combobox(window)
difficulty_combo["values"] = ["Easy","Medium","Hard"]
difficulty_combo.current(0)
difficulty_combo.pack(pady=5)

# Buttons
btn1 = tk.Button(window,text="Generate 3 Questions",
                 command=lambda:generate_questions(3))
btn1.pack(pady=5)

btn2 = tk.Button(window,text="Generate 100 Questions",
                 command=lambda:generate_questions(100))
btn2.pack(pady=5)

# Output box
result_box = tk.Text(window,height=15,width=65)
result_box.pack(pady=10)

window.mainloop()
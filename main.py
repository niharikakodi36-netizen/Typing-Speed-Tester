import tkinter as tk
import random
import time

# Load paragraphs
with open("paragraphs.txt", "r", encoding="utf-8") as file:
    paragraphs = [line.strip() for line in file if line.strip()]

if not paragraphs:
    raise RuntimeError("No paragraphs found in paragraphs.txt. Add some non-empty lines.")

start_time = 0

# Start typing test
def start_test(event):
    global start_time
    if start_time == 0:
        start_time = time.time()

# Calculate result
def calculate_result():
    global start_time

    end_time = time.time()
    total_time = end_time - start_time

    typed_text = text_input.get("1.0", tk.END).strip()
    original_text = paragraph_label["text"].strip()

    typed_words = len(typed_text.split())
    wpm = round((typed_words / total_time) * 60) if total_time > 0 else 0

    correct_chars = 0
    for i in range(min(len(typed_text), len(original_text))):
        if typed_text[i] == original_text[i]:
            correct_chars += 1

    accuracy = round((correct_chars / len(original_text)) * 100) if original_text else 0

    result_label.config(
        text=f"WPM: {wpm} | Accuracy: {accuracy}%"
    )

# Restart test
def restart_test():
    global start_time
    start_time = 0

    random_paragraph = random.choice(paragraphs)

    paragraph_label.config(text=random_paragraph)
    text_input.delete("1.0", tk.END)
    result_label.config(text="")

# GUI Window
root = tk.Tk()
root.title("Typing Speed Tester")
root.geometry("700x400")

title_label = tk.Label(
    root,
    text="Typing Speed Tester",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

paragraph_label = tk.Label(
    root,
    text=random.choice(paragraphs),
    wraplength=600,
    font=("Arial", 14)
)
paragraph_label.pack(pady=20)

text_input = tk.Text(root, height=7, width=70, font=("Arial", 12))
text_input.pack()

text_input.bind("<KeyPress>", start_test)

submit_button = tk.Button(
    root,
    text="Submit",
    command=calculate_result,
    font=("Arial", 12)
)
submit_button.pack(pady=10)

restart_button = tk.Button(
    root,
    text="Restart",
    command=restart_test,
    font=("Arial", 12)
)
restart_button.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=20)

root.mainloop()
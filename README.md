# Typing Speed Tester Using Python

A simple and interactive Typing Speed Tester application developed using Python and Tkinter. This project helps users improve their typing speed and accuracy by calculating Words Per Minute (WPM) and typing accuracy in real time.

---

## Features

- Random paragraph generation
- Typing speed calculation (WPM)
- Accuracy calculation
- User-friendly graphical interface
- Restart functionality
- Paragraph storage using text file

---

## Technologies Used

- Python
- Tkinter
- File Handling

---

## Project Structure

TypingSpeedTester/
│
├── main.py
├── paragraphs.txt
└── README.md

---

## How It Works

1. The application displays a random paragraph from `paragraphs.txt`.
2. The user types the paragraph in the text area.
3. After clicking the submit button, the application calculates:
   - Words Per Minute (WPM)
   - Typing Accuracy
4. The restart button loads a new paragraph for practice.

---

## WPM Formula

WPM = (Number of Words Typed / Time Taken in Seconds) × 60

---

## Accuracy Formula

Accuracy = (Correct Characters / Total Characters) × 100

---

## Installation and Execution

### Step 1: Install Python

Download Python from:
https://www.python.org

---

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/TypingSpeedTester.git
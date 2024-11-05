from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f"{quiz_brain}",
            fill=THEME_COLOR,
            font=("Arial", 10, "italic")
        )
        true_image = PhotoImage(file="day34/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="day34/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2, column=1)
        self.next_question()
        self.window.mainloop()
    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.false_button.config(state="active")
            self.true_button.config(state="active")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
    def click(self):
        self.false_button.config(state="disabled")
        self.true_button.config(state="disabled")
        self.window.after(1000, self.next_question)
    def true_press(self):
        correct = self.quiz.check_answer("true")
        self.update_score()
        self.feedback(correct)
        self.click()
    def false_press(self):
        correct = self.quiz.check_answer("false")
        self.update_score()
        self.feedback(correct)
        self.click()
    def feedback(self, answer):
        if answer == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
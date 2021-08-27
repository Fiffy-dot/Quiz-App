from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=FONT,
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=correct_image, highlightthickness=0, command=self.true_selected)
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_selected)
        self.correct_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have finished the quiz!")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_selected(self):
        user_ans = "True"
        is_correct = self.quiz.check_answer(user_ans)
        self.give_feedback(is_correct)

    def false_selected(self):
        user_ans = "False"
        is_correct = self.quiz.check_answer(user_ans)
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

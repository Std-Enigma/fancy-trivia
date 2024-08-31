from tkinter import *

from quiz_brain import QuizBrain

CANVAS_WIDTH, CANVAS_HEIGHT = 300, 250
MAIN_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:

        self.quiz = quiz_brain

        self.amount = 0

        self.window = Tk()
        self.window.title(string="Quizzler")
        self.window.configure(padx=20, pady=20, background=MAIN_COLOR)

        self.canvas = Canvas(
            master=self.window,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
        )
        self.canvas_text = self.canvas.create_text(
            CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, width=280, font=FONT, fill=MAIN_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(
            master=self.window,
            text=f"Score: {self.quiz.score}",
            background=MAIN_COLOR,
            foreground="white",
            font=FONT,
        )
        self.score_label.grid(row=0, column=1)

        self.check_mark_image = PhotoImage(name="True", file="images/true.png")
        self.true_button = Button(
            highlightthickness=0,
            image=self.check_mark_image,
            command=lambda: self.button_action(answer="True"),
        )
        self.true_button.grid(row=2, column=0)

        self.x_mark_image = PhotoImage(name="False", file="images/false.png")
        self.false_button = Button(
            highlightthickness=0,
            image=self.x_mark_image,
            command=lambda: self.button_action(answer="False"),
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if not self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfigure(self.canvas_text, text=question)
        else:
            self.canvas.configure(background="white")
            self.canvas.itemconfigure(
                self.canvas_text, text="You have reached the end of the quiz."
            )
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")

    def update_score(self):
        self.score_label.configure(text=f"Score: {self.quiz.score}")

    def update_ui(self):
        self.update_score()
        self.canvas.configure(background="white")
        self.get_next_question()

    def button_action(self, answer: str):
        if self.quiz.check_answer(answer):
            self.canvas.configure(background="green")
        else:
            self.canvas.configure(background="red")
        self.window.after(1000, func=self.update_ui)

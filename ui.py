from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text= "Place Holder:\nNew Question here.",
            fill=THEME_COLOR,
            font=("Arial", 20,"italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", foreground= "white", background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(highlightthickness=0, image=true_img, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(highlightthickness=0, image=false_img, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        #처음 프로그램을 실행할 때 question placeholder가 보이지 않도록...
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text="It's end of the quizzler!")
            # 두 개 버튼 비활성화 시키기
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            # update the canvas's text (UI에 제공)
            self.canvas.itemconfig(self.question_text, text=q_text)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # 0.5초 후, 다음 질문 제공하기
        self.window.after(500, func=self.get_next_question)


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)



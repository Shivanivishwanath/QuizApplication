from tkinter import *
from quiz_brain import Quiz_brain

THEME_COLOR="#375362"

class QuizInterface:
    def __init__(self, quiz_brain: Quiz_brain):
        self.quiz= quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=2, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font= 60)
        self.score_label.grid(row=0, column= 1)
        self.canvas= Canvas(width=300,height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        true_image = PhotoImage(file="images/true1.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2,column=0)
        false_image = PhotoImage(file="images/false1.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        # self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.get_next_q()
        self.window.mainloop()

    def get_next_q(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_ques()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of game \n Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")



    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)

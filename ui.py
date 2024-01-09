THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class UserInterface():
    def __init__(self,quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title('QuizApp')
        self.window.config(background=THEME_COLOR,padx=20,pady=20)

        self.score_label = Label(text='Score: 0',background=THEME_COLOR,fg='#ffffff')
        self.score_label.grid(column=1,row=0)

        self.quiz_brain=quiz_brain

        self.canvas = Canvas(background='#ffffff',height=250,width=300)
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='sample text', 
            font=('Arial',16,'italic'))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        true_img = PhotoImage(file='day_34\\images\\true.png')
        false_img = PhotoImage(file='day_34\\images\\false.png')

        self.true_button = Button(image=true_img,highlightthickness=0,command=self.set_true)
        self.true_button.grid(column=0,row=2)
        
        self.false_button = Button(image=false_img,highlightthickness=0,command=self.set_false)
        self.false_button.grid(column=1,row=2)
        self.next_question()
        self.window.mainloop()

    def set_true(self):
        is_right = self.quiz_brain.check_answer('true')
        self.give_feedback(is_right)

    def set_false(self):
        is_right=self.quiz_brain.check_answer('false')
        self.give_feedback(is_right)

    def next_question(self):        
        self.canvas.config(background='white')
        if self.quiz_brain.still_has_questions():
            self.update_score()
            next_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=next_question)
        else:
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            self.canvas.itemconfig(self.canvas_text, text='Quiz end')
            
            reload_button = Button(text='START AGAIN',command=reload)
            reload_button.grid(row=3,column=2)

    def reload():
        
    def update_score(self):
        score = f'Score: {self.quiz_brain.score}'
        self.score_label.config(text=score)

            

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(background='green')
        else: 
            self.canvas.config(background='red')
        self.window.after(1000,self.next_question)

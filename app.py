
import tkinter as tk
from tkinter import messagebox


class Main (tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container=tk.Frame(self,width=500, height=700)
        container.pack (side="top", fill="both",expand=True)
        container.grid_rowconfigure(0, weight=1, minsize=700)
        container.grid_columnconfigure(0, weight=1,minsize=500)
        self.frames={}
        self.selectedAnswers=tk.IntVar()
        self.correctAnswers=0
        self.score=0
        self.questionsAnswered=0
        for F in (WelcomePage, InstructionPage,Question1,Question2, Question3,Question4,Question5,Question6,Question7,Question8,Question9,Question10, Restart):
            page_name=F.__name__
            frame=F(parent=container, controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame("WelcomePage")
    def show_frame(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()
    def end_game(self):
        self.destroy()
    def correctAnswer(self,questionNum):
        self.correctAnswers+=1
        self.score+=10
        self.questionsAnswered+=1
        if self.questionsAnswered>=10:
            messagebox.showinfo(title="Game over!", message="Your final score is "+str(self.score))
            self.show_frame("Restart")
        else:
            messagebox.showinfo(title="Correct Answer", message="Correct! Your current score is "+str(self.score))
            frame=self.frames[questionNum]
            frame.tkraise()
    def wrongAnswer(self,questionNum):
        self.questionsAnswered+=1
        if self.questionsAnswered>=10:
            messagebox.showinfo(title="Game over", message="Sorry, that's wrong! Your final score is " + str(self.score))
            self.show_frame("Restart")
        else:
            messagebox.showinfo(title="Wrong answer", message="Sorry! That's wrong. Your current score is " + str(self.score))
            frame = self.frames[questionNum]
            frame.tkraise()
class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500,height=700, bg="#F5DFF0")
        self.controller=controller
        title=tk.Label(self, text="STEMsational Women: Trivia Trailblazers", wraplength=400, font=("Modern No. 20",40, 'bold'),
                       bg="#F5DFF0",fg="#E16D92",justify="center")
        title.place(anchor="center", y=100,x=250)
        photo=tk.PhotoImage(file="logo.png")
        logo=tk.Label(self,image=photo,borderwidth=0)
        logo.image=photo
        logo.place(x=250,y=350,anchor="center")
        next = tk.Button(self, text="Welcome!", command=lambda: [controller.show_frame("InstructionPage")],
                     bg="#A54AE3", font=("Modern No. 20", 35), fg="#FAFDF6", activebackground="#AE8AE4")
        next.place(anchor="center", x=250, y=550)
class InstructionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg="#AE8AE4")
        self.controller=controller
        title = tk.Label(self, text="How To Play", wraplength=400,
                         font=("Modern No. 20", 40),
                         bg="#AE8AE4", fg="#F5DFF0", justify="center")
        title.place(anchor="center", y=100, x=250)
        photo = tk.PhotoImage(file="inst.png")
        logo = tk.Label(self, image=photo, borderwidth=0)
        logo.image = photo
        logo.place(x=250, y=400, anchor="center")
        instructions = tk.Label(self, text="This game is all about famous women in STEM. Answer the questions"
                                           " that follow! You receive ten points for each correct answer!"
                                , wraplength=400, font=("Modern No. 20", 20),
                                bg="#AE8AE4", fg="#F5DFF0", justify="center")
        instructions.place(anchor="center", y=150, x=250)
        start = tk.Button(self, text="Click here to start!", command=lambda: controller.show_frame("Question1"),
                          bg="#D99CC8", font=("Modern No. 20", 20), fg="#FAFDF6", activebackground="#E16D92")
        start.place(anchor="center", x=250, y=600)
        instructions.place(anchor="center", y=200, x=250)
        title.place(anchor="center", x=250, y=50)

class Question1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg = "#CB69A7")
        self.controller=controller
        question=tk.Label(self, text="1. What physicist is famous for her work on nuclear physics and was awarded two Nobel Prizes?",wraplength=400,font=("Modern No. 20", 20, 'bold'), bg = "#CB69A7", fg = '#F5DFF0')
        question.place(anchor="center",x=250,y=100)
        choices=["Maria Goeppert Mayer","Dorothy Crowfood Hodgkin","Barbara McClintock","Marie Curie"]
        opt1=tk.Button(self,text=choices[0],command=lambda:controller.wrongAnswer("Question2"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt2 = tk.Button(self, text=choices[1], command=lambda: controller.wrongAnswer("Question2"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt3 = tk.Button(self, text=choices[2], command=lambda: controller.wrongAnswer("Question2"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt4 = tk.Button(self, text=choices[3], command=lambda: controller.correctAnswer("Question2"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt1.place(anchor="center", x=250, y=270)
        opt2.place(anchor="center", x=250, y=370)
        opt3.place(anchor="center", x=250, y=470)
        opt4.place(anchor="center", x=250, y=570)
class Question2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg = "#CB69A7")
        self.controller=controller
        question=tk.Label(self, text="2. Who is famous for her work on Dark Matter and Dark Energy in astrophysics?",wraplength=400,font=("Modern No. 20", 20, 'bold'), bg = "#CB69A7", fg = '#F5DFF0')
        question.place(anchor="center",x=250,y=100)
        choices=["Rachel Carson","Vera Rubin","Mae Jemison","Maria Goeppert Mayer"]
        opt1=tk.Button(self,text=choices[0],command=lambda:controller.wrongAnswer("Question3"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt2 = tk.Button(self, text=choices[1], command=lambda: controller.correctAnswer("Question3"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt3 = tk.Button(self, text=choices[2], command=lambda: controller.wrongAnswer("Question3"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt4 = tk.Button(self, text=choices[3], command=lambda: controller.wrongAnswer("Question3"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt1.place(anchor="center", x=250, y=270)
        opt2.place(anchor="center", x=250, y=370)
        opt3.place(anchor="center", x=250, y=470)
        opt4.place(anchor="center", x=250, y=570)
class Question3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg = "#CB69A7")
        self.controller=controller
        question=tk.Label(self, text="3. Who was the first Hispanic woman to go into space and later was the head of NASA’s Johnson Space Center?",wraplength=400,font=("Modern No. 20", 20, 'bold'), bg = "#CB69A7", fg = '#F5DFF0')
        question.place(anchor="center",x=250,y=100)
        choices=["Rachel Carson","Ellen Ochoa","Maria Goeppert Mayer","Caroline Hershel"]
        opt1=tk.Button(self,text=choices[0],command=lambda:controller.wrongAnswer("Question4"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt2 = tk.Button(self, text=choices[1], command=lambda: controller.correctAnswer("Question4"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt3 = tk.Button(self, text=choices[2], command=lambda: controller.wrongAnswer("Question4"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt4 = tk.Button(self, text=choices[3], command=lambda: controller.wrongAnswer("Question4"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt1.place(anchor="center", x=250, y=270)
        opt2.place(anchor="center", x=250, y=370)
        opt3.place(anchor="center", x=250, y=470)
        opt4.place(anchor="center", x=250, y=570)
class Question4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg = "#CB69A7")
        self.controller=controller
        question=tk.Label(self, text="4. Who is known for her research on the environmental effects of synthetic pesticides and wrote a book titles “Silent Spring”?",wraplength=400,font=("Modern No. 20", 20, 'bold'), bg = "#CB69A7", fg = '#F5DFF0')
        question.place(anchor="center",x=250,y=100)
        choices=["Barbara McClintock","Grace Hopper","Rachel Carson","May-Britt Moser"]
        opt1=tk.Button(self,text=choices[0],command=lambda:controller.wrongAnswer("Question5"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt2 = tk.Button(self, text=choices[1], command=lambda: controller.wrongAnswer("Question5"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt3 = tk.Button(self, text=choices[2], command=lambda: controller.correctAnswer("Question5"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt4 = tk.Button(self, text=choices[3], command=lambda: controller.wrongAnswer("Question5"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt1.place(anchor="center", x=250, y=270)
        opt2.place(anchor="center", x=250, y=370)
        opt3.place(anchor="center", x=250, y=470)
        opt4.place(anchor="center", x=250, y=570)
class Question5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg = "#CB69A7")
        self.controller=controller
        question=tk.Label(self, text="5. Who became the first African-American woman to travel in space in 1992?",wraplength=400,font=("Modern No. 20", 20, 'bold'), bg = "#CB69A7", fg = '#F5DFF0')
        question.place(anchor="center",x=250,y=100)
        choices=["Mae Jemison","Vera Rubin","Jocelyn Bell Burnell","Maria Skłodowska-Curie"]
        opt1=tk.Button(self,text=choices[0],command=lambda:controller.correctAnswer("Question6"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt2 = tk.Button(self, text=choices[1], command=lambda: controller.wrongAnswer("Question6"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt3 = tk.Button(self, text=choices[2], command=lambda: controller.wrongAnswer("Question6"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt4 = tk.Button(self, text=choices[3], command=lambda: controller.wrongAnswer("Question6"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt1.place(anchor="center", x=250, y=270)
        opt2.place(anchor="center", x=250, y=370)
        opt3.place(anchor="center", x=250, y=470)
        opt4.place(anchor="center", x=250, y=570)

class Question6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg = "#CB69A7")
        self.controller=controller
        question=tk.Label(self, text="6. Which woman is known for her research in primatology and her extensive study of chimpanzees in Tanzania?",wraplength=400,font=("Modern No. 20", 20, 'bold'), bg = "#CB69A7", fg = '#F5DFF0')
        question.place(anchor="center",x=250,y=100)
        choices=["Ada Lovelace","Jane Goodall","Rosalind Franklin","Barbra McClintock"]
        opt1=tk.Button(self,text=choices[0],command=lambda:controller.wrongAnswer("Question7"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt2 = tk.Button(self, text=choices[1], command=lambda: controller.correctAnswer("Question7"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt3 = tk.Button(self, text=choices[2], command=lambda: controller.wrongAnswer("Question7"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt4 = tk.Button(self, text=choices[3], command=lambda: controller.wrongtAnswer("Question7"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt1.place(anchor="center", x=250, y=270)
        opt2.place(anchor="center", x=250, y=370)
        opt3.place(anchor="center", x=250, y=470)
        opt4.place(anchor="center", x=250, y=570)
class Question7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg = "#CB69A7")
        self.controller=controller
        question=tk.Label(self, text="7. Who is a renowned geneticist and developmental biologist known for her discovery of mobile genetic elements (aka jumping genes)?",wraplength=400,font=("Modern No. 20", 20, 'bold'), bg = "#CB69A7", fg = '#F5DFF0')
        question.place(anchor="center",x=250,y=100)
        choices=["Barbara McClintock","Rita-Levi Montalcini","Jocelyn Bell Burnell","Maria Skłodowska-Curie"]
        opt1=tk.Button(self,text=choices[0],command=lambda:controller.correctAnswer("Question8"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt2 = tk.Button(self, text=choices[1], command=lambda: controller.wrongAnswer("Question8"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt3 = tk.Button(self, text=choices[2], command=lambda: controller.wrongAnswer("Question8"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt4 = tk.Button(self, text=choices[3], command=lambda: controller.wrongAnswer("Question8"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt1.place(anchor="center", x=250, y=270)
        opt2.place(anchor="center", x=250, y=370)
        opt3.place(anchor="center", x=250, y=470)
        opt4.place(anchor="center", x=250, y=570)
class Question8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg = "#CB69A7")
        self.controller=controller
        question=tk.Label(self, text="8. Who is a leading neuroscientist recognized for her work on understanding the neural mechanisms of learning, memory, and neurodegenerative diseases like Alzheimer's?",wraplength=400,font=("Modern No. 20", 20, 'bold'), bg = "#CB69A7", fg = '#F5DFF0')
        question.place(anchor="center",x=250,y=100)
        choices=["Maria Goeppert Mayer","May-Britt Moser","Rita-Levi Montalcini","Susumu Tonegawa"]
        opt1=tk.Button(self,text=choices[0],command=lambda:controller.wrongAnswer("Question9"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt2 = tk.Button(self, text=choices[1], command=lambda: controller.wrongAnswer("Question9"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt3 = tk.Button(self, text=choices[2], command=lambda: controller.wrongAnswer("Question9"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt4 = tk.Button(self, text=choices[3], command=lambda: controller.correctAnswer("Question9"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt1.place(anchor="center", x=250, y=270)
        opt2.place(anchor="center", x=250, y=370)
        opt3.place(anchor="center", x=250, y=470)
        opt4.place(anchor="center", x=250, y=570)
class Question9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg = "#CB69A7")
        self.controller=controller
        question=tk.Label(self, text="9. Which chemist won the Nobel Prize in Chemistry for her work on the structure of important biochemical substances, including penicillin and vitamin B12?",wraplength=400,font=("Modern No. 20", 20, 'bold'), bg = "#CB69A7", fg = '#F5DFF0')
        question.place(anchor="center",x=250,y=100)
        choices=["Jocelyn Bell Burnell","Ada Lovelace","Dorothy Crowfoot Hodgkin","Grace Hopper"]
        opt1=tk.Button(self,text=choices[0],command=lambda:controller.wrongAnswer("Question10"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt2 = tk.Button(self, text=choices[1], command=lambda: controller.wrongAnswer("Question10"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt3 = tk.Button(self, text=choices[2], command=lambda: controller.correctAnswer("Question10"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt4 = tk.Button(self, text=choices[3], command=lambda: controller.wrongAnswer("Question10"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt1.place(anchor="center", x=250, y=270)
        opt2.place(anchor="center", x=250, y=370)
        opt3.place(anchor="center", x=250, y=470)
        opt4.place(anchor="center", x=250, y=570)
class Question10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700, bg = "#CB69A7")
        self.controller=controller
        question=tk.Label(self, text="10. Who is known for being the world’s first computer programmer and for her early work on computers?",wraplength=400,font=("Modern No. 20", 20, 'bold'), bg = "#CB69A7", fg = '#F5DFF0')
        question.place(anchor="center",x=250,y=100)
        choices=["Ada Lovelace","Maria Skłodowska-Curie","Grace Hopper","May-Britt Moser"]
        opt1=tk.Button(self,text=choices[0],command=lambda:controller.correctAnswer("Question10"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt2 = tk.Button(self, text=choices[1], command=lambda: controller.wrongAnswer("Question10"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt3 = tk.Button(self, text=choices[2], command=lambda: controller.wrongAnswer("Question10"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt4 = tk.Button(self, text=choices[3], command=lambda: controller.wrongAnswer("Question10"), font=("Modern No. 20", 15), fg = '#F5DFF0', bg = '#AE8AE4')
        opt1.place(anchor="center", x=250, y=270)
        opt2.place(anchor="center", x=250, y=370)
        opt3.place(anchor="center", x=250, y=470)
        opt4.place(anchor="center", x=250, y=570)
class Restart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,width=500, height=700,bg="#F5DFF0" )
        self.controller=controller
        restart=tk.Label(self, text="Do you want to play again?",font = ("Modern No. 20",25, 'bold'),wraplength=400,bg="#F5DFF0", fg="#E16D92")
        restart.place(anchor="center",x=250,y=200)
        opt1=tk.Button(self,text="Yes",command=lambda: controller.show_frame("InstructionPage"), fg="#F5DFF0", font=("Modern No. 20", 20), bg = '#E16D92' )
        opt2 = tk.Button(self, text="No", command=lambda: controller.end_game(), fg="#F5DFF0", font=("Modern No. 20", 20), bg = '#E16D92')
        opt1.place(x=150,y=400,anchor="center")
        opt2.place(x=350,y=400,anchor="center")
if __name__== '__main__':
    app=Main()
    app.mainloop()


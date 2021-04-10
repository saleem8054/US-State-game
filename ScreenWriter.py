from turtle import Turtle
class ScreenWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("normal")
        
        
    def writeToScreen(self,state_name,position):
        self.goto(position)
        self.write(state_name)
    
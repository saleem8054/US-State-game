from ScreenWriter import ScreenWriter
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen_writer = ScreenWriter()
data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()

screen_title = "Guess the state"
correct_guess = 0
guess_states = []
missing_states = []

while correct_guess != 50:
    answer_state = screen.textinput(title=screen_title,prompt="write another state's name: ").title()
    
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guess_states]
        break
    if answer_state:
        if answer_state in states_list:
            details = data[data["state"] == answer_state]
            x_coordinate = details.x.item()
            y_coordinate = details.y.item()
            screen_writer.writeToScreen(answer_state,(x_coordinate,y_coordinate))
            correct_guess += 1
            screen_title = f"{correct_guess}/50 States Correct"
            guess_states.append(answer_state)
            states_list.remove(answer_state)
            
    else:
        screen_title = "Please insert any state's name"
        



result_dic = {"States":missing_states}

df = pandas.DataFrame(result_dic)
df.to_csv("learn.csv")
import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Guess Philippine Provinces")
image = "PH_MAP.gif"
screen.addshape(image)
turtle.shape(image)

Philippine_data = pd.read_csv("province_coordinate1.csv", encoding='latin1')
all_provinces = Philippine_data.Provinces.to_list()
guessed_provinces = []
lives = 5

while len(guessed_provinces) < 86:
    answer_province = screen.textinput(title=f"{len(guessed_provinces)}/86 Provinces Correct", prompt="How many provinces can you guess on the Philippine map?").title()

    if answer_province == "Exit":
        get_all_not_guessed = []
        for provinces in all_provinces:
            if provinces not in guessed_provinces:
                get_all_not_guessed.append(provinces)

        create_new_dataFrame = pd.DataFrame(get_all_not_guessed)
        create_new_dataFrame.to_csv("provinces_to_learn.csv")
        break
    if answer_province in all_provinces:
        guessed_provinces.append(answer_province)
        text = turtle.Turtle()
        shape = turtle.Turtle()

        shape.penup()
        shape.shape("circle")
        shape.color("red")
        shape.shapesize(.5)

        province_data = Philippine_data[Philippine_data.Provinces == answer_province]
        shape.goto(x=province_data.x.item(), y=province_data.y.item())
        text.hideturtle()
        text.penup()
        text.goto(x=province_data.x.item(), y=province_data.y.item() + 5)
        text.color("black")
        text.write(answer_province, font=("Arial", 8, "bold"))


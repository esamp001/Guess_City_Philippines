import turtle
import pandas as pd
from text_turtle import GuessedText

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Guess Philippine Provinces")
image = "PH_MAP.gif"
screen.addshape(image)
turtle.shape(image)

Philippine_data = pd.read_csv("province_coordinate1.csv", encoding='latin1')
all_provinces = Philippine_data.Provinces.to_list()

answer_province = screen.textinput(title="Guess the Province",prompt="How many provinces can you guess on the Philippine map?")
print(answer_province)

if answer_province in all_provinces:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.shape("circle")
    t.color("red")
    t.shapesize(.5)
    province_data = Philippine_data[Philippine_data.Provinces == answer_province]
    t.goto(x=province_data.x.item(), y=province_data.y.item())





screen.exitonclick()
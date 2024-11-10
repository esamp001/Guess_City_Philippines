import turtle
from text_turtle import GuessedText

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Guess Philippine Provinces")
image = "PH_MAP.gif"
screen.addshape(image)
turtle.shape(image)

text = GuessedText()
text.get_coordinates_in_csv()



screen.exitonclick()
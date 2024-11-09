import turtle
import pandas as pd

Philippine_data = pd.read_csv("province_coordinate1.csv", encoding='latin1')

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Guess Philippine Provinces")
image = "PH_MAP.gif"
screen.addshape(image)
turtle.shape(image)

answer_province = screen.textinput(title="Guess the Province", prompt="How many provinces can you guess on the Philippine map?")


if answer_province in Philippine_data["Provinces"].values:
    # Get the corresponding 'Coordinates' for the matching province
    coordinates = Philippine_data.loc[Philippine_data["Provinces"] == answer_province, "Coordinates"].values[0]
    print(coordinates)
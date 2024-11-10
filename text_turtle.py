from turtle import Turtle,Screen
import pandas as pd
from turtle import Screen

Philippine_data = pd.read_csv("province_coordinate1.csv", encoding='latin1')

class GuessedText(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(1)

    def get_coordinates_in_csv(self):
        screen = Screen()
        answer_province = screen.textinput(title="Guess the Province",prompt="How many provinces can you guess on the Philippine map?")
        if answer_province in Philippine_data["Provinces"].values:
            # Get the corresponding 'Coordinates' for the matching province
            coordinates = Philippine_data.loc[Philippine_data["Provinces"] == answer_province, "Coordinates"].values[0]
            print(coordinates)



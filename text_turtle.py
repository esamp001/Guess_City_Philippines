from turtle import Turtle,Screen
import pandas as pd

Philippine_data = pd.read_csv("province_coordinate1.csv", encoding='latin1')


class GuessedText(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(.5)


    def get_coordinates_in_csv(self):
        screen = Screen()
        answer_province = screen.textinput(title="Guess the Province",prompt="How many provinces can you guess on the Philippine map?")
        coordinates = Philippine_data.loc[Philippine_data['Provinces'] == answer_province, 'Coordinates'].values
        if answer_province in Philippine_data["Provinces"]:
            x, y = map(float, coordinates.split(','))
            print(x)
            print(y)











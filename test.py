# provinces = []
# save_coordinates = []
#
# Philippine_data = pd.read_csv("province.csv", encoding='latin1')
#
# for province in Philippine_data.description:
#     provinces.append(province)
# def get_mouse_click_coor(x, y):
#     save_coordinates.append((x, y))
#     print(f"({x}, {y})")
#
# turtle.onscreenclick(get_mouse_click_coor) #Call the getmouse click coor function
#
# turtle.mainloop() #Actively Listen for events
#
#
#
# data_dict = {
#     "Provinces": provinces,
#     "Coordinates": save_coordinates
# }
# max_length = max(len(lst) for lst in data_dict.values())
#
# for key, lst in data_dict.items():
#     lst.extend([None] * (max_length - len(lst)))
#
#
# print(data_dict["Coordinates"])
#
# create_new_dataFrame = (pd.DataFrame(data_dict))
# print(create_new_dataFrame)
# create_new_dataFrame.to_csv("province_coordinate1.csv", index=False)
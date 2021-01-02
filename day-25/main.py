# with open("weather_data.csv") as data_file:
# 	data = data_file.readlines()
# 	print(data)

# import csv
# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temperatures = []
# 	for row in data:
# 		if row[1] != "temp":
# 			temperatures.append(int(row[1]))
# 	print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# # print(data.temp.max())
# # print(data.condition)
#
# print(data[data.temp == data.temp.max()].condition)
#
# # Create a DataFrame from scratch
#
# data_dic = {
#     "students": ["Amy", "James", "Anngela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dic)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colors = ["Gray", "Cinnamon", "Black"]
output_dic = {
    "Fur Color": [],
    "Count": [],
}
for color in fur_colors:
    output_dic["Fur Color"].append(color)
    output_dic["Count"].append(len(data[data["Primary Fur Color"] == color]))

output = pandas.DataFrame(output_dic)
output.to_csv("squirrel_count.csv")
# print(output_dic)

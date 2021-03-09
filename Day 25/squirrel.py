import pandas
data = pandas.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_color = data["Primary Fur Color"]
print (primary_color)
color_count= primary_color.value_counts().to_dict()
print (color_count)

color_dic = { 
        "Primary Furr Color":["Gray","Cinnamon", "Black"],
        "Count": [color_count["Gray"], color_count["Cinnamon"], color_count["Black"]]
}

new_data =  pandas.DataFrame(color_dic)
print (new_data)
new_data.to_csv("Day 25/squirrel_color.csv")
#print(data.groupby("Primary Fur Color").count())


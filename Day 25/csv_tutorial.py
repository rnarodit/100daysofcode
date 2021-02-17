# with open("Day 25/weather_data.csv") as csv_data:
#     data = csv_data.readlines()
#     print (data)

# import csv # allows us to easily work with CSV files
# with open("Day 25/weather_data.csv") as csv_data:
#     data = csv.reader(csv_data) # read CSV file
#     # print (data)
#     tempratures = []
   
#     for row in data: # each row in data is a list
        
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
    
#     print (tempratures)

#Pandas is a python data analysis library 
import pandas
data = pandas.read_csv("Day 25/weather_data.csv")
# print (type(data))
# print (data ["temp"]) # print specific coloumn via its name 
# pandas data frame object is equivalent to an entire table
# pandas series object is equivalent to a single column in your table

# data_dict = data.to_dict()
# print (data_dict)

# temp_list = data["temp"].to_list() # convert coloumn to list
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)

# # a simpler way to calc the avg temp
# print (data["temp"].mean())
# print(data["temp"].max())

# #get data in coloumn:
# print (data["condition"])
# #or
# print(data.condition)

#get data in rows:
# print (data[data.day == "Monday"]) # get a hold of data table and then specify coloumn to look through  and the value too look for in that coloumn
# print (data[data.temp == data.temp.max()])

# # accessing a specific value in a row 
# monday = data[data.day == "Monday"]
# print (monday.condition) 
# temparture = (int(monday.temp) * (9/5))+32
# print (temparture)

#create data frame from scratch
data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
print (new_data)
new_data.to_csv("Day 25/new_data.csv")
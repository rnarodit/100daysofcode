#application programming interface-> set of commands , functions, protocols . and objects that programmers can use to create software or interact with an external system
#API is interface between your program into an external system
#API endpoint -> the location to which you turn to in order to use the API data, location where API data can be found
#API request -> how you get data from an API
#Bank analogy -> bank address (API endpoint), (API bank teller), (Data bank vault), send requests to teller to get data

import requests
from datetime import datetime
MY_LAT= 38.795021
MY_LONG= -77.273300
# response= requests.get(url="http://api.open-notify.org/iss-now.json")
# #print(response)
# print(response.status_code)
# response.raise_for_status()
#response codes : 1xx -> Hold on 2xx:here you go, everything successful 3xx-> you don't have premission go away 4xx(client)-> you screwed up, thing u looking for might not even exist 5xx-> I(server) screwed up , website is down for example

# data = response.json()
# #data = response.json()["iss_position"]["longitude"]
# longitude= data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude,latitude)
# print (iss_position)

#API parameters -> allows u to give input when making API requests to change the result you recieve
# not all APIs have parameters 
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]#separating the long time string into separate elements in a list and accessing the hour
sunset= data["results"]["sunset"].split("T")[1].split(":")[0]#separating the long time string into separate elements in a list and accessing the hour
print (sunrise)
print(sunset) 

time_now = datetime.now ()
print(time_now.hour)


#when requesting with parameters they are apendeded to url with '?' follower by parameter and '&' used to add more parameters 
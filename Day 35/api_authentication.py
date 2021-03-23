#free api -> completely free no payment tier, simple data that isn't v expensive to collect
#Charging for APIs -> a way of selling data that was complicated to collect and analyze 
# API Key -> similar to personal account number and password. this is how API provider can track how much you are using the API and to authorize/deny your access 
import requests
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

MY_LAT= 0
MY_LONG= 0
api_key= ""
parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "exclude":"current,minutely,daily",
    "appid":api_key
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"]
weather_codes = [data[hour]["weather"][0]["id"] for hour in range(0,11) ]

will_rain= False
for id in weather_codes:
    if (id <700):
        will_rain = True

if(will_rain == False):
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Don't Forget to bring an Umbrella ☂️",
                     from_='',
                     to=''
                 )
    print(message.status)

#enviornment variables -> can set set variables as enviornment variables so u don't need to change the code if u want to make a change to their value(convinience)
    #security ->not good to have authenticationkeys to be stored in the same place as your code. enviornment variables allows to store our secure api keys away from the code base and keep em secret 

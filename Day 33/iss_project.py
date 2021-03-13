import requests
from datetime import datetime
import smtplib
import time

MY_LAT= 38.795021
MY_LONG= -77.273300
while True:
    time.sleep(60)
    email = "pavlinx1aws@gmail.com"
    password="F5Id7sK3zLx8"
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

    if ((-5<= MY_LAT-iss_latitude <=55 ) and (-5 <= MY_LONG-iss_longitude <=5) and (time_now.hour>sunset or time_now._hour < sunrise )):
        with smtplib.SMTP("smtp.gmail.com") as connection :
            connection.starttls()#trasnport layer security, a way to secure connection to email server and prevent from other people from reading it in transit
            connection.login(user=email, password= password)
            connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:ISS Close\n\nLook Up!" )# sending motivational quote for yourself
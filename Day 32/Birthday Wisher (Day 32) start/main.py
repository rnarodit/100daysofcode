import smtplib
import datetime as dt
import random

email = "pavlinx1aws@gmail.com"# you email here
password="F5Id7sK3zLx8"
# #connection = smtplib.SMTP("smtp.gmail.com") #a way to conncet to email provider smtp server

# with smtplib.SMTP("smtp.gmail.com") as connection :
#     connection.starttls()#trasnport layer security, a way to secure connection to email server and prevent from other people from reading it in transit
#     connection.login(user=email, password= password)
#     connection.sendmail(from_addr=email, to_addrs= "hundreddaysofcode99@yahoo.com", msg="Subject:hello\n\nthis is the body of my email" )
# #connection.close()

#import datetime as dt
now = dt.datetime.now()
#year= now.year
#month = now.month
day_of_week = now.weekday()
print(day_of_week)

quotes= open("Day 32/Birthday Wisher (Day 32) start/quotes.txt", "r")
quote_list=quotes.read().splitlines()
quotes.close()

if (day_of_week == 2):
    quote = random.choice(quote_list)
    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()#trasnport layer security, a way to secure connection to email server and prevent from other people from reading it in transit
        connection.login(user=email, password= password)
        connection.sendmail(from_addr=email, to_addrs= email, msg=f"Subject:\n\n{quote}" )# sending motivational quote for yourself



date_of_birth = dt.datetime(year=1995, month=8, day=17) #only month year and day are required to create a datetime object
print (date_of_birth)
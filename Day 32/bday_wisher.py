##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt

email = "pavlinx1aws@gmail.com"
password="F5Id7sK3zLx8"
# 1. Update the birthdays.csv
bday_data = pandas.read_csv("Day 32/birthdays.csv")
birthday_dict= bday_data.to_dict(orient="records")


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

for birthday in birthday_dict:
    if (month == birthday["month"] and day == birthday["day"]):
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        bday_name =birthday["name"]
        letter_num =random.randint(1,3)
        with open (f"Day 32/letter_templates/letter_{letter_num}.txt" ) as letter:
            letter_contents = letter.read()
            print(letter_contents)
            new_letter = letter_contents.replace("[NAME]",bday_name)
            print(new_letter)
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection :
            connection.starttls()#trasnport layer security, a way to secure connection to email server and prevent from other people from reading it in transit
            connection.login(user=email, password= password)
            connection.sendmail(from_addr=email, to_addrs="hundreddaysofcode99@yahoo.com", msg=f"Subject:\n\n{new_letter}" )# sending motivational quote for yourself
print(day)



# 4. Send the letter generated in step 3 to that person's email address.





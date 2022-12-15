import datetime as dt
import random

now=dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday()
print(day_of_week)

day_of_week_list={
    0:"Monday",
    1:"Tuesday",
    2:"Wednesday",
    3:"Thursday",
    4:"Friday",
    5:"Saturday",
    6:"Sunday"
}


date_of_birth=dt.datetime(year=1995,month=12,day=15,hour=4)
print(date_of_birth)


if day_of_week in day_of_week_list:
    print(day_of_week_list[day_of_week])
else:
    print("no está")

with open("quotes.txt") as f:
    lines=f.readlines()
    print(type(lines))
    pick_line=random.choice(lines)
    print(pick_line)


import smtplib

my_email="anaidbrachomolina@gmail.com"
password="jnlxikwrixoxbrux"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="itzelbrachomolina@gmail.com",
        msg=f"Subject:{day_of_week_list[day_of_week]} Motivation \n\n{pick_line}")

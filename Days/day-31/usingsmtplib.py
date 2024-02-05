import smtplib

my_email = "random@gmail.com"
password = "abcd1234"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="somerandom@gmail.com", 
        msg="Subject:This is an example\n\nThis is the body of the example"
    )

import datetime as dt

now = dt.datetime.now() #gives you current date and time
year = now.year

import smtplib
import time

my_email = "XXXXXXX@gmail.com" # Your email address
my_password = "YYYYYYYYYYYY" # Your email App Password (setup through security settings)

#Infinite doom spam below can be time based or not using a while true loop
#time.sleep(5)
#while True:
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
    from_addr=my_email,
    to_addrs=my_email,
    msg="Subject:YOU'VE BEEN HACKED BY JROC\n\n import time\n - time.sleep(5)\n while true LOOOOOP\n NAWHATI'M SAYING??????"
    )

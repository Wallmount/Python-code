# Program that tracks ISS and sends the 
# user an email reminder every time the ISS
#  passes the users position, and is visible 
# (e. g. when it is dark).

import requests
import datetime
import smtplib
import time

#Fill in your latitude, longitude, email and password. Fill in the email that you want to send emails to.
MY_LAT = 0.0
MY_LONG = 0.0
MY_EMAIL = ""
PASSWORD = ""
TO_EMAIL = ""

time_now = datetime.datetime.now()

# ISS DATA
def iss_is_close():
    '''Gets ISS position from API and returns True if ISS position is close to your position.'''
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if (iss_latitude >= MY_LAT-5 and iss_latitude <= MY_LAT+5) and (iss_longitude >= MY_LONG-5 and iss_longitude <= MY_LONG+5):
        return True


# SUNRISE DATA
def night_time():
    '''Checks which hour the sun sets and rises at your position with data from API and returns True 
    if the current time is between sunset and sunrise, e. g. it is dark.'''

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise_data = response.json()

    sunrise_hour = int(sunrise_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sunrise_data["results"]["sunset"].split("T")[1].split(":")[0])
    now_hour = time_now.hour

    if now_hour >= sunset_hour or now_hour <= sunrise_hour:
        return True

# SEND EMAIL IF ISS IS NEAR AND IT IS NIGHT TIME (DARK)
while True:
    time.sleep(60)
    if iss_is_close() and night_time():

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=f"Subject:ISS is passing right now!\n\nLook up!")
        connection.close()

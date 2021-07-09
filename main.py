import requests
import time
from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "(your email id)"
MY_PASSWORD = (your email password)

today = datetime.now()
today_tuple = (today.month, today.day)

OWN_ENDPOINT = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=734001&date=12-06-2021"
auth_token = (visit cowin api tab and create your auth token)
parameter = {
    "BearerAuth": (visit cowin api tab and create your auth )
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
response = requests.get(url=OWN_ENDPOINT, headers=headers)
response.raise_for_status()
data = response.json()
# print(data)

#

def availability():
    c = False
    centers = data["centers"]
    success_message = ""
    success_messages = []
    for center in centers:
        if center["sessions"][0]["min_age_limit"] == 18 and center['sessions'][0]['available_capacity'] > 0:
            c = True
            message = f"Vaccination center: {center['name']}\n" \
                      f"Center Address: {center['address']}\n" \
                      f" Date: {center['sessions'][0]['date']}\n " \
                      f"Number of Vaccines Available:{center['sessions'][0]['available_capacity']}\n " \
                      f"Fee Type: {center['fee_type']}\n"\
                      f"Timing: From {center['from']} to {center['to'] }\n " \
                      f"Vaccine: {center['sessions'][0]['vaccine']}\n " \
                      f"Visit cowin.gov.in website and book your slot for {center['name'] } on {center['sessions'][0]['date']}"
            success_messages.append(message)
            success_message = "\n\n".join(success_messages)

    if c:
        return success_message
    else:
        print("Sleep")

        time.sleep(30)
        print("Wake")
        availability()


# Function triggers if slot available
content = availability()
print(content)
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=(enter a target valid email id),
        msg=(f"Subject:Vaccine Slot Alert !!!\n\n{content}"))

print("Mail sent successfully")
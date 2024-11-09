print("""



                   -----------------------------------



                       WELCOME TO MY MENU PROJECT



                   -----------------------------------



""")



# Importing necessary modules

from twilio.rest import Client

import requests

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from googlesearch import search

import schedule

import time

import numpy as np

import pywhatkit as pyw

import cv2

import sys

import os

import geocoder

from datetime import datetime 

import pyttsx3

from playsound import playsound



print("Press 1 to send WhatsApp message")

print("Press 2 to send a text message")

print("Press 3 to make a call")

print("Press 4 to send an email")

print("Press 5 to scrape top 5 results for any search on Google")

print("Press 6 to schedule an email")

print("Press 7 to collect data and store them")

print("Press 8 to collect data and send WhatsApp messages")

print("Press 9 to capture video")

print("Press 10 to display rainbow text")

print("Press 11 to display date command of another system")

print("Press 12 to schedule live streaming broadcast and send link by sms python")

print("Press 13 to find the current geo coordinates and location")

print("Press 14 to convert text to audio")



def collect_data():

    data = []

    for i in range(5):

        print(f"Collecting data for team member {i + 1}:")

        name = input("Enter Name: ")

        city = input("Enter City: ")

        college = input("Enter College: ")

        whatsapp_number = input("Enter WhatsApp Number: ")

        life_purpose = input("Enter Life Purpose (in max 5 words): ")

        data.append([name, city, college, whatsapp_number, life_purpose])

    return np.array(data)



def send_whatsapp_messages(numbers):

    for number in numbers:

        pyw.sendwhatmsg_instantly(f"+{number}", "Hi, LW Welcomes you")



x = input("Enter your choice: ")



if int(x) == 1:

    account_sid = 'ACb37be1d43700e63eccd1af55484261f9'

    auth_token = 'dfc1e11585d70ccbfc7b5cd0226d1fb4'

    client = Client(account_sid, auth_token)

    from_whatsapp_number = 'whatsapp:+14155238886'

    to_whatsapp_number = 'whatsapp:+919460991588'

    message_body = 'Hello, this is Anushka'

    message = client.messages.create(

        body=message_body,

        from_=from_whatsapp_number,

        to=to_whatsapp_number

    )

    print(f"WhatsApp message sent with SID: {message.sid}")



elif int(x) == 2:

    resp = requests.post('https://textbelt.com/text', {

        'phone': '+919460991588',

        'message': 'Hello I am learning',

        'key': 'textbelt'

    })

    print(resp.json())



elif int(x) == 3:

    account_sid = "ACb37be1d43700e63eccd1af55484261f9"

    auth_token = "dfc1e11585d70ccbfc7b5cd0226d1fb4"

    client = Client(account_sid, auth_token)

    call = client.calls.create(

        twiml='<Response><Say>Welcome to Just Code</Say></Response>',

        to='+919460991588',

        from_='+13858992123'

    )

    print(call.sid)



elif int(x) == 4:

    email = "anushkaranjan141113@gmail.com"

    reciever_email = "ranjananushka29@gmail.com"

    subject = input("Subject: ")

    message = input("Message: ")

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(email, "nfxv pmgj zqcp udwj")

    server.sendmail(email, reciever_email, message)

    print("Email has been sent to", reciever_email)



elif int(x) == 5:

    query = input("Enter your search query: ")

    num_results = 5

    search_results = search(query, num_results=num_results)

    for i, result in enumerate(search_results, start=1):

        print(f"{i}. {result}")



elif int(x) == 6:

    email = "anushkaranjan141113@gmail.com"

    reciever_email = "ranjananushka29@gmail.com"

    password = "nfxv pmgj zqcp udwj"



    def send_email():

        subject = input("Subject: ")

        message = input("Message: ")

        msg = MIMEMultipart()

        msg['From'] = email

        msg['To'] = reciever_email

        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        try:

            server = smtplib.SMTP("smtp.gmail.com", 587)

            server.starttls()

            server.login(email, password)

            server.sendmail(email, reciever_email, msg.as_string())

            print("Email has been sent to", reciever_email)

        except Exception as e:

            print(f"Failed to send email: {e}")

        finally:

            server.quit()



    def schedule_email(time_str):

        schedule.clear()

        schedule.every().day.at(time_str).do(send_email)

        print(f"Email scheduled at {time_str} every day.")

        while True:

            schedule.run_pending()

            time.sleep(1)



    time_str = input("Enter the time to send the email (HH:MM in 24-hour format): ")

    schedule_email(time_str)



elif int(x) == 7:

    team_data = collect_data()

    print("\nCollected Data:")

    print("Name\t\tCity\t\tCollege\t\tWhatsapp Number\t\tLife Purpose")

    for row in team_data:

        print("\t\t".join(row))



elif int(x) == 8:

    team_data = collect_data()

    print("\nCollected Data:")

    print("Name\t\tCity\t\tCollege\t\tWhatsApp Number\t\tLife Purpose")

    for row in team_data:

        print("\t\t".join(row))

    subarray = team_data[:, 3]  

    send_whatsapp_messages(subarray)



elif int(x) == 9:

    cap = cv2.VideoCapture("http://192.168.43.182:8080/video")

    while True:

        status, photo = cap.read()

        if not status:

            break

        cv2.imshow("new photo", photo)

        if cv2.waitKey(1) == 13:  

            break

    cap.release()

    cv2.destroyAllWindows()



elif int(x) == 10:

    def rainbow_text(text):

        colors = [

            '\033[91m',  # Red

            '\033[93m',  # Yellow

            '\033[92m',  # Green

            '\033[96m',  # Cyan

            '\033[94m',  # Blue

            '\033[95m',  # Magenta

        ]

        reset = '\033[0m'  # Reset color to default

        while True:

            for start in range(len(colors)):

                rainbow_line = ''

                for i, char in enumerate(text):

                    rainbow_line += f'{colors[(start + i) % len(colors)]}{char}'

                rainbow_line += reset  

                sys.stdout.write(f'\r{rainbow_line}')

                sys.stdout.flush()

                time.sleep(0.1)  



    text = input("Enter your text: ")

    rainbow_text(text)

    

elif int(x) == 11:

     os.system("ssh 198.168.251.204 date")



elif int(x) == 12:

    account_sid = 'AC0af4136ba6fc94229c32d874de8128f3'

    auth_token = '5cfe255efdc7b08049f72539312be03c'

    twilio_number = '+14027994726'

    recipient_number = '+919410822102'

    live_stream_url = 'https://your-live-stream-url'



    def send_sms():

        client = Client(account_sid, auth_token)

        message = client.messages.create(

            body=f"Your live stream is starting now! Watch it here: {live_stream_url}",

            from_=twilio_number,

            to=recipient_number

        )

        print(f"SMS sent at {datetime.now()}: {message.sid}")



    def schedule_live_stream(hour, minute):

        schedule_time = f"{hour:02d}:{minute:02d}"

        schedule.every().day.at(schedule_time).do(send_sms)

        print(f"Live stream scheduled at {schedule_time} daily.")



    schedule_live_stream(15, 52)



    while True:

        schedule.run_pending()

        time.sleep(1)



elif int(x) == 13:

    g = geocoder.ip('me')

    latitude, longitude = g.latlng

    print(f"Latitude: {latitude}, Longitude: {longitude}")

    location = g.city + ", " + g.state + ", " + g.country

    print(f"Location: {location}")

    

    

elif int(x) == 14:

     def text_to_audio(text, filename='output.wav'):

         engine = pyttsx3.init()

         engine.setProperty("rate", 150)
         engine.setProperty("volume", 1)

         engine.save_to_file(text, filename)
         engine.runAndWait()

         print(f"Audio saved as {filename}")

         playsound(filename)

     text = input("Enter the text you want to convert to audio: ")

     text_to_audio(text)





else:

    print("Invalid choice. Please enter a number from 1 to 14.")


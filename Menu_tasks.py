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

import smtplib
 
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from instagrapi import Client

import subprocess

import requests

from bs4 import BeautifulSoup

import urllib.parse

import pyfiglet

import pymongo

import boto3

import json




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

print("Press 15 to Send Email from Linux Terminal")

print("Press 16 to Use linux as a zoom server")

print("Press 17 to Make a post in telegram, instagram, facebook, discord from the linux terminal")

print("Press 18 to Change the color of files and folder in linux")

print("Press 19 to Read the entire RAM")

print("Press 20 to Change the look and feel of GNOME terminal")

print("Press 21 To create user and set password")

print("Press 22 to Run linux in the browser")

print("Press 23 to Google search from terminal")

print("Press 24 to Run Windows softwares e.g notepad in linux")

print("Press 25 to Sync two different folders in linux. It should ask the user which folders to sync")

print("Press 26 to On your cmd to print something and it will be converted to ASCII art")

print("Press 27 to Launch ec2 instances in AWS")

print("Press 28 to Launch EC2 instance with RHEL GUI")

print("Press 29 to Access logs from the cloud (CloudWatch)")

print("Press 30 to Event-driven architecture for audio transcription")

print("Press 31 to Connect Python to MongoDB using Lambda")

print("Press 32 to Upload an object to S3")

print("Press 33 to Integrate Lambda with S3 and SES to send emails")



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



elif int(x) == 15:

     def send_email(sender_email, sender_password, recipient_email, subject, body):

        msg = MIMEMultipart()

        msg['From'] = sender_email

        msg['To'] = recipient_email

        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))



        try:

            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()

            server.login(sender_email, sender_password)

            server.send_message(msg)

            print("Email sent successfully!")

        except Exception as e:

            print(f"Failed to send email: {e}")

        finally:

            server.quit()



     sender_email = "anushkaranjan141113@gmail.com"

     sender_password = input("Enter your email password: ")

     recipient_email = input("Enter the recipient's email: ")

     subject = input("Enter the subject of the email: ")

     body = input("Enter the body of the email: ")

     send_email(sender_email, sender_password, recipient_email, subject, body)

elif int(x) == 16:

     def run_command(command):

        print(f"Executing: {command}")

        os.system(command)



     def setup_jitsi_meet():

        run_command("yum update -y")

        hostname = "www.streetkart.online"

        run_command(f"hostnamectl set-hostname {hostname}")

        run_command("yum install -y epel-release")

        run_command("yum install -y nginx certbot java-11-openjdk")

        repo_content = """[jitsi]

 name=Jitsi

 baseurl=https://download.jitsi.org/stable/

 gpgcheck=1

 gpgkey=https://download.jitsi.org/jitsi-key.gpg.key"""



     with open("/etc/yum.repos.d/jitsi-stable.repo", "w") as repo_file:

            repo_file.write(repo_content)


     run_command("yum install -y jitsi-meet")

     run_command("/usr/share/jitsi-meet/scripts/install-letsencrypt-cert.sh")

     run_command("firewall-cmd --permanent --add-port=80/tcp")

     run_command("firewall-cmd --permanent --add-port=443/tcp")

     run_command("firewall-cmd --permanent --add-port=10000/udp")

     run_command("firewall-cmd --reload")

     run_command("systemctl start nginx")

     run_command("systemctl enable nginx")

     run_command("systemctl start jitsi-videobridge2")

     run_command("systemctl enable jitsi-videobridge2")

     run_command("systemctl start jicofo")

     run_command("systemctl enable jicofo")

     run_command("systemctl start prosody")

     run_command("systemctl enable prosody")



     print(f"Jitsi Meet server setup complete. Access it at https://{hostname}")



     if __name__ == "__main__":

        setup_jitsi_meet()



elif int(x) == 17:

     USERNAME = 'visvasa_heal'

     PASSWORD = 'Visvasa@1234'



     def post_to_instagram(image_path, caption):

        cl = Client()

        cl.login(USERNAME, PASSWORD)

        cl.photo_upload(image_path, caption)

     post_to_instagram('e:\Users\hp\Downloads\LOGO.jpeg', 'Hello from Visvasa!')



elif int(x) == 18:


     COLORS = {

        'reset': '\033[0m',

        'red': '\033[31m',

        'green': '\033[32m',

        'yellow': '\033[33m',

        'blue': '\033[34m',

        'magenta': '\033[35m',

        'cyan': '\033[36m',

        'white': '\033[37m'

    }



     def colorize(text, color):

        return f"{COLORS[color]}{text}{COLORS['reset']}"



     def list_colored_files_and_folders(directory):

         for item in os.listdir(directory):

             if os.path.isdir(os.path.join(directory, item)):

                print(colorize(item, 'blue')) 

             else:

                print(colorize(item, 'green')) 



     list_colored_files_and_folders(".")  



elif int(x) == 19:

    print("Feature not yet implemented.")



elif int(x) == 20:


     def set_gnome_terminal_preference(schema, key, value):

        command = ["gsettings", "set", schema, key, value]

        subprocess.run(command, check=True)

        print(f"Set {key} to {value} for {schema}")



     def change_gnome_terminal_look_and_feel():

        profile_id = "org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:<profile_id>/"

        font = input("Enter the font you want to use (e.g., 'Monospace 12'): ")

        set_gnome_terminal_preference(profile_id, "font", f"'{font}'")

        bg_color = input("Enter the background color in HEX (e.g., '#000000' for black): ")

        set_gnome_terminal_preference(profile_id, "background-color", f"'{bg_color}'")

        fg_color = input("Enter the foreground color in HEX (e.g., '#FFFFFF' for white): ")

        set_gnome_terminal_preference(profile_id, "foreground-color", f"'{fg_color}'")

        use_transparent_bg = input("Use transparent background? (true/false): ").lower()

        if use_transparent_bg == 'true':

            transparency = input("Enter transparency level (0 to 1, e.g., 0.5): ")

            set_gnome_terminal_preference(profile_id, "use-transparent-background", "true")

            set_gnome_terminal_preference(profile_id, "background-transparency-percent", str(int(float(transparency) * 100)))

        else:

            set_gnome_terminal_preference(profile_id, "use-transparent-background", "false")

            dark_theme = input("Use dark theme? (true/false): ").lower()

            set_gnome_terminal_preference(profile_id, "use-theme-colors", "false")

            set_gnome_terminal_preference(profile_id, "use-theme-transparency", "false")

            set_gnome_terminal_preference("org.gnome.desktop.interface", "gtk-theme", "'Adwaita-dark'" if dark_theme == 'true' else "'Adwaita'")

        change_gnome_terminal_look_and_feel()



elif int(x) == 21:



     def create_user(username, password):

        try:

            subprocess.run(['useradd', '-m', username], check=True)

            print(f"User '{username}' created successfully.")

            subprocess.run(['chpasswd'], input=f'{username}:{password}'.encode(), check=True)

            print(f"Password for user '{username}' set successfully.")

        except subprocess.CalledProcessError as e:

            print(f"An error occurred: {e}")

            print(f"Failed to create user '{username}' or set password.")



     def main():

        username = input("Enter the username: ")

        password = input("Enter the password: ")

        create_user(username, password)



     if __name__ == "__main__":

        main()



elif int(x) == 22:

     def google_search(query):

        query = urllib.parse.quote_plus(query)

        url = f"https://www.google.com/search?q={query}"

        headers = {

            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",

        }

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        for g in soup.find_all('div', class_='BVG0Nb'):

            a_tag = g.find('a')

            if a_tag:

                link = a_tag['href']

                print(f"Title: {a_tag.text}")

                print(f"Link: {link}\n")



        if __name__ == "__main__":

         query = input("Enter your search query: ")

        google_search(query)



elif int(x) == 23:

    print("Feature not yet implemented.")



elif int(x) == 24:

    def sync_folders(source_folder, destination_folder):

        if not os.path.isdir(source_folder):

            print(f"Source folder does not exist: {source_folder}")

            return

        if not os.path.isdir(destination_folder):

            print(f"Destination folder does not exist: {destination_folder}")

            return

        rsync_command = [

            'rsync',

            '-av',          

            '--delete',      

            source_folder + '/', 

            destination_folder

        ]



        try:

            result = subprocess.run(rsync_command, capture_output=True, text=True)

            print("Output:")

            print(result.stdout)

            print("Errors:")

            print(result.stderr)

            if result.returncode == 0:

                print("Sync completed successfully!")

            else:

                print("Sync failed with errors.")

        except FileNotFoundError:

            print("rsync command not found. Please install rsync.")

        except Exception as e:

            print(f"An error occurred: {e}")



    if __name__ == "__main__":

        source_folder = input("Enter the path to the source folder: ")

        destination_folder = input("Enter the path to the destination folder: ")

        sync_folders(source_folder, destination_folder)



elif int(x) == 25:

    def text_to_ascii():

        text = input("Enter the text you want to convert to ASCII art: ")

        ascii_art = pyfiglet.figlet_format(text)

        print(ascii_art)



    text_to_ascii()



elif int(x) == 26:

    def create_ec2_instance():

        ec2 = boto3.resource('ec2')

        instances = ec2.create_instances(

            ImageId='ami-0c55b159cbfafe1f0',

            MinCount=1,

            MaxCount=1,

            InstanceType='t2.micro',

            KeyName='your-key-pair'

        )

        for instance in instances:

            print(f"EC2 instance {instance.id} created.")



    create_ec2_instance()



elif int(x) == 27:

    def launch_rhel_gui():

        ec2 = boto3.resource('ec2')

        instances = ec2.create_instances(

            ImageId='ami-0e4d38ebd047c3d1a',

            MinCount=1,

            MaxCount=1,

            InstanceType='t2.micro',

            KeyName='your-key-pair',

            UserData='''

            #!/bin/bash

            yum update -y

            yum groupinstall -y "Server with GUI"

            systemctl set-default graphical.target

            systemctl isolate graphical.target

            '''

        )

        for instance in instances:

            print(f"RHEL GUI EC2 instance {instance.id} created.")



    launch_rhel_gui()



elif int(x) == 28:

    def access_cloudwatch_logs():

        log_group_name = input("Enter the log group name: ")

        log_stream_name = input("Enter the log stream name: ")



        logs_client = boto3.client('logs')

        response = logs_client.get_log_events(

            logGroupName=log_group_name,

            logStreamName=log_stream_name

        )



        for event in response['events']:

            print(f"Timestamp: {event['timestamp']} - Message: {event['message']}")



    access_cloudwatch_logs()



elif int(x) == 29:

    def transcribe_audio(event, context):

        s3 = boto3.client('s3')

        transcribe = boto3.client('transcribe')

        bucket = event['Records'][0]['s3']['bucket']['name']

        key = event['Records'][0]['s3']['object']['key']

        job_name = f"TranscriptionJob_{key}"

        job_uri = f"s3://{bucket}/{key}"



        transcribe.start_transcription_job(

            TranscriptionJobName=job_name,

            Media={'MediaFileUri': job_uri},

            MediaFormat='mp3',

            LanguageCode='en-US'

        )



        print(f"Started transcription job for {key}")



    transcribe_audio(event, context)



elif int(x) == 30:

    def lambda_handler(event, context):

        client = boto3.client('secretsmanager')

        secret_name = "your_mongodb_secret"

        response = client.get_secret_value(SecretId=secret_name)

        secret = json.loads(response['SecretString'])

        uri = secret['MONGODB_URI']



        mongo_client = pymongo.MongoClient(uri)

        db = mongo_client['your_database']

        collection = db['your_collection']



        document = event['document']

        result = collection.insert_one(document)



        return {

            'statusCode': 200,

            'body': json.dumps(f"Document inserted with ID: {result.inserted_id}")

        }



elif int(x) == 31:

    def upload_to_s3():

        s3 = boto3.client('s3')

        bucket_name = 'your_bucket_name'

        file_name = input("Enter the file name to upload: ")

        object_name = input("Enter the S3 object name: ")



        try:

            s3.upload_file(file_name, bucket_name, object_name)

            print(f"{file_name} uploaded to {bucket_name}/{object_name}")

        except Exception as e:

            print(f"Error uploading file: {e}")



    upload_to_s3()



elif int(x) == 32:

    def lambda_s3_ses_handler(event, context):

        s3_client = boto3.client('s3')

        ses_client = boto3.client('ses')

        bucket = event['Records'][0]['s3']['bucket']['name']

        key = event['Records'][0]['s3']['object']['key']

        email_body = f"File {key} was uploaded to {bucket}"



        response = ses_client.send_email(

            Source='your_email@example.com',

            Destination={'ToAddresses': ['recipient@example.com']},

            Message={

                'Subject': {'Data': 'S3 Upload Notification'},

                'Body': {'Text': {'Data': email_body}}

            }

        )

        print("Email sent.")



    lambda_s3_ses_handler(event, context)



else:

    print("Invalid choice. Please enter a number from 1 to 33.")


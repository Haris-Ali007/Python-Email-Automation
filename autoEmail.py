# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 23:53:59 2021

@author: Haris
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def create_conn(host, port):
    smtp_obj = smtplib.SMTP(host = host, port = port)
    smtp_obj.starttls()
    smtp_obj.ehlo() 
    return smtp_obj


def get_contacts():
    contacts = []
    with open('contacts.txt', 'r') as contacts_file:
        for contact in contacts_file:
            contacts.append(contact)
    return contacts

def get_message():
    #reading message from a text file
    with open('message.txt', 'r') as file:
        message = file.read()
    return message


#taking sender id and pswd
email = input("Enter you email id:\n ")
pswd = input("Enter your password:\n")
subj = input("Enter email subject:\n")

#get contacts   
contacts = get_contacts()

#get message body
message = get_message()

#connecting with smtp server
#host and port for connecting with an outlook smtps server
smtp_obj = create_conn(host= 'smtp-mail.outlook.com', port= 587)
smtp_obj.login(email, pswd)

i = 1
#creating and sending an email
for contact in contacts:
    #creating an email
    msg_obj = MIMEMultipart()
    msg_obj['From'] = email
    msg_obj['To'] = contact
    msg_obj['Subject'] = subj
    msg_obj.attach(MIMEText(message, 'plain'))

    #sending message
    smtp_obj.send_message(msg_obj)
    print('\n Mail sent to {} successfully.'.format(contact))
    del msg_obj
smtp_obj.quit()

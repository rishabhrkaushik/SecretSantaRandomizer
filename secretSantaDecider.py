# File Name: secretSantaDecider.py
# Author: Rishabh Kaushik
# Description: This code generates random number and creates matches for Secret Santa based on that. On matching it sends an automated email to the Secret Santa as to whom they have to send gifts to.

from random import randint # for randon number generation
import smtplib # for sending automated email

# the codes allows to have groups. Group 1 will send group to only people from group 2 and vice versa.
# make sure both groups have equal number of people.
sender1 = ["P1", "P2", "P3", "P4"]
receiver1 = ["P5", "P6", "P7", "P8"]

sender2 = ["P5", "P6", "P7", "P8",]
receiver2 = ["P1", "P2", "P3", "P4"]

# email id of the account from which email would be sent
myemail = 'email@domail.com'
mypassword = 'somepassword'

message = """From: Sender Name <{0}>
To: {1} <{2}>
Subject: Santa is coming!!!

Hi {3},
Hope you had a wonderful year. Let's end this well by spreading joy.
Fate (Randomized Python Script :p) has selected you to bring joy in the life of {4}.
Send them gifts and love on the following address.

{5}
"""


people  = {
    "P1": {
        "firstName": "Mr. One",
        "fullName": "Person 1",
        "email": "person1@domain.com",
        "address": "Person 1, Person 1 lives here"
    },
    "P2": {
        "firstName": "Mr. Two",
        "fullName": "Person 2",
        "email": "person2@domain.com",
        "address": "Person 2, Person 2 lives here"
    },
    "P3": {
        "firstName": "Mr. Three",
        "fullName": "Person 3",
        "email": "person3@domain.com",
        "address": "Person 3, Person 3 lives here"
    },
    "P4": {
        "firstName": "Mr. Four",
        "fullName": "Person 4",
        "email": "person4@domain.com",
        "address": "Person 4, Person 4 lives here"
    },
    "P5": {
        "firstName": "Mr. Five",
        "fullName": "Person 5",
        "email": "person5@domain.com",
        "address": "Person 5, Person 5 lives here"
    },
    "P6": {
        "firstName": "Mr. Six",
        "fullName": "Person 6",
        "email": "person6@domain.com",
        "address": "Person 6, Person 6 lives here"
    },
    "P7": {
        "firstName": "Mr. Seven",
        "fullName": "Person 7",
        "email": "person7@domain.com",
        "address": "Person 7, Person 7 lives here"
    },
    "P8": {
        "firstName": "Mr. Eight",
        "fullName": "Person 8",
        "email": "person8@domain.com",
        "address": "Person 8, Person 8 lives here"
    },

}

try:
    # replace address and port with mail configuration file if not using gmail
    # for gmail, you need to turn on "less secure app access" for the script to be able to login
    session = smtplib.SMTP('smtp.gmail.com',587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(myemail, mypassword)
except smtplib.SMTPException:
    print('Error')

def sendMail(senderInitial, receiverInitial):
    try:
        session.sendmail(myemail, [people[senderInitial]["email"]], message.format(myemail, people[senderInitial]["fullName"], people[senderInitial]["email"], people[senderInitial]["firstName"], people[receiverInitial]["firstName"], people[receiverInitial]["address"]))
    except smtplib.SMTPException:
        print('Error')

# while(not (len(sender1) == 0 and len(sender2) == 0)):
for sender in ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]:
    # sender = input("Enter the initials of sender in capitals: ")

    if sender in sender1:
        sender1.remove(sender)
        receiver = receiver1[randint(0, len(receiver1) - 1)]
        # print(receiver)
        sendMail(sender, receiver)
        receiver1.remove(receiver)
    elif sender in sender2:
        sender2.remove(sender)
        receiver = receiver2[randint(0, len(receiver2) - 1)]
        # print(receiver)
        sendMail(sender, receiver)
        receiver2.remove(receiver)
    else:
        print("Wrong Initials")

session.quit()

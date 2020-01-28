import fbchat
from fbchat import Client
from getpass import getpass
username = input("Username: ")
#username = "EAMIL"
Client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name: "))
    friends = Client.searchForUsers(name)
    friend = friends[0]
    msg = str(input("Message: "))
    loop = int(input("Loops: "))
    for loop in range(1,loop+1):
        sent = Client.send(fbchat.models.Message(msg), friend.uid)
    if sent:
        print("Message sent successfully!")
import fbchat
from fbchat import Client
from getpass import getpass
import time
#username = input("Username: ")
username = "taypzaangel_427@hotmail.com"
Client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name: "))
    friends = Client.searchForUsers(name)
    friend = friends[0]
    msg = str(input("Message: "))
    loop = int(input("Loops: "))
    times = int(input("Delays: "))
    for loop in range(1,loop+1):
        time.sleep(times)
        sent = Client.send(fbchat.models.Message(msg), friend.uid)
        print("Loops:", loop, "Message:", msg)
    if sent:
        print("Message sent successfully!")

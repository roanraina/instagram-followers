from dotenv import load_dotenv
import os
from instagrapi import Client

# load enviroment variables
load_dotenv()
USERNAME = os.environ.get("IG_USERNAME")
PASSWORD = os.environ.get("IG_PASSWORD")

# Get User Id
cl = Client()
cl.login(USERNAME, PASSWORD)

user_id = cl.user_id_from_username("roanraina")

print("User Id: " + str(user_id) + "\n")

# Get users who follow you
cl = Client()
cl.login(USERNAME, PASSWORD)

followers = cl.user_followers(user_id, 0)

print("followed by: " + str(len(followers)) + " users")

# Get users you follow
cl = Client()
cl.login(USERNAME, PASSWORD)

following = cl.user_following(user_id, 0)

print("following: " + str(len(following)) + " users")


# Find users who dont follow you back

dont_follow_back = following.keys() - followers.keys()

print("\nUsers who dont follow you back (" + str(len(dont_follow_back)) + "):")

for user_id in dont_follow_back: 
    print(following[user_id].username)

# Find users you dont follow back
dont_follow =  followers.keys() - following.keys()

print("\nUsers you dont follow back (" + str(len(dont_follow)) + "):")

for user_id in dont_follow: 
    print(followers[user_id].username)
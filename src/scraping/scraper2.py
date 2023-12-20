import praw
import requests
import re
import os
from dotenv import load_dotenv

# relative path
current_directory = os.path.dirname(__file__)
os.chdir(current_directory)

# get the vars
load_dotenv()

ID = os.environ.get("ID")
SECRET = os.environ.get("SECRET")
USERAGENT = os.environ.get("USERAGENT")
PWR = os.environ.get("PWR")



def scrape_post(sub, output_folder="./pics"):
    # Initialize the Reddit API client
    reddit = praw.Reddit(client_id=ID,
                         client_secret=SECRET,
                         user_agent=USERAGENT,
                         password=PWR,
                         username=USER)
    print(reddit.user.me())

scrape_post("blackcats")

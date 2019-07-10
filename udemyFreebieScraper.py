import praw
from credentials import *


reddit = praw.Reddit(client_id = c_id, client_secret = c_secret, user_agent = u_agent, user_name= u_name, password= u_pass)

subred = reddit.subreddit("udemyfreebies").top('day')
for i in new:
  print(i.title)

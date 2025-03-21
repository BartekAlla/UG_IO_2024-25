import praw
import pandas as pd

reddit = praw.Reddit(client_id='HTVytU19QAcZUFmdyc1e5g',
                     client_secret='HycrzE0BB9GV8Mj8F9KhbKFGKeJKiw',
                     user_agent='BartlaTest u/test')

topic = "Python"

posts = []

for submission in reddit.subreddit('all').search(topic, limit=100):
    posts.append([submission.created_utc, submission.id, submission.title, submission.url])

df = pd.DataFrame(posts, columns=["Date", "ID", "Title", "URL"])

df.to_csv("reddit_posts.csv", index=False)

print(f"Pobrano 100 postów na temat '{topic}' z Reddita.")

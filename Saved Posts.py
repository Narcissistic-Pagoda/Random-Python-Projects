import praw
import pandas as pd

# Initialize PRAW with your Reddit API credentials
reddit = praw.Reddit(client_id='IgvH0zWfWvq1I34c5pGAwA',
                     client_secret='joM4HkbD26sArcYOmWXKr5xpc_sTkw',
                     username='munamadan_reuturns',
                     password='dIp@n2718281828',
                     user_agent='MySavedPostsExportBot/1.0')

# Get all saved posts for the authenticated user
saved_posts = reddit.user.me().saved(limit=None)

# Create a list to store the relevant data for each post
posts_data = []
for post in saved_posts:
    post_data = {'Title': post.title,
                 'URL': post.url,
                 'Subreddit': post.subreddit.display_name,
                 'Author': post.author.name,
                 'Score': post.score,
                 'Created': post.created_utc,
                 'Body': post.selftext}
    posts_data.append(post_data)

# Convert the list of post data into a Pandas DataFrame
df = pd.DataFrame(posts_data)

# Save the DataFrame to an Excel spreadsheet
df.to_excel('saved_posts.xlsx', index=False)

import snscrape.modules.twitter as sntwitter
import time

def scrape_tweets(query, num_tweets):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        print(f'this is the {i}th tweet: {tweet}')
        time.sleep(10) 
        tweets.append({
            'content': tweet.content,
            'date': tweet.date,
            'username': tweet.user.username,
            'retweets': tweet.retweetCount,
            'likes': tweet.likeCount
        })

        if i + 1 >= num_tweets:
            break  # Break out of the loop when num_tweets is reached

    return tweets

# Example usage:
query = "#datascience"
num_tweets = 10  # Set the desired number of tweets
result = scrape_tweets(query, num_tweets)
print(result)

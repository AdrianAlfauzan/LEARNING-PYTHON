import tweepy
from textblob import TextBlob

# Mengatur kredensial Twitter
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Mengautentikasi dengan API Twitter menggunakan Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def analisis_sentimen(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity


def main():
    # Mencari tweet berdasarkan kata kunci
    search_query = "Python programming"
    tweets = tweepy.Cursor(api.search, q=search_query, lang="en").items(10)

    for tweet in tweets:
        print(f"Tweet: {tweet.text}")
        sentiment_score = analisis_sentimen(tweet.text)
        print(
            f"Sentimen: {'Positif' if sentiment_score > 0 else 'Negatif' if sentiment_score < 0 else 'Netral'}"
        )
        print()


if __name__ == "__main__":
    main()

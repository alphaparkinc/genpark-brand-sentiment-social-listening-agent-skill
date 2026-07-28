from client import SocialListeningClient

def main():
    client = SocialListeningClient()
    res = client.analyze_sentiment(mentions=['Great app!', 'Terrible support'])
    print(f"Result for sentiment_ratio: {res['sentiment_ratio']}")

if __name__ == "__main__":
    main()

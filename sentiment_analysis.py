import json
import boto3
import os

## This file is building out ability to take in text and analyze the sentiment of it

class sentiment_analyzer:
    def __init__(self) -> None:
        self.session = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
        )

    # text = audience suggestion
    def get_sentiment(self, text): ##using AWS service to pull key words
        comprehend = self.session.client(service_name='comprehend', region_name='us-west-2')

        print('Getting sentiment from text...')

        response = json.loads(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
        
        sentiment = response['Sentiment']
        sentiment_score = response['SentimentScore']

        return sentiment, sentiment_score






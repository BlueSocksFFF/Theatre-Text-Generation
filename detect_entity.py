import json
import boto3
from dotenv import load_dotenv
import os

load_dotenv()


class entity_extractor:
    def __init__(self) -> None:
        self.session = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
        )

    # text = raw scene text
    def get_entities(self, text): ##using AWS service to pull entities
        comprehend = self.session.client(service_name='comprehend', region_name='us-west-2')

        print('Extracting key words from text...')

        response = json.loads(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))['Entities']
        
        ##this setup creates a list in each type so that multiple entities will be grouped together if they share
        # the same type. We may not want that down the road.
        entities = {}
        for entity in response:
            entity_type = entity['Type']
            entity_text = entity['Text']
            if entity_type not in entities:
                entities[entity_type] = []
            entities[entity_type].append(entity_text)
        return entities



## testing  
  
# raw_audience_speech = "I have never lived in New York City, but my mother Dorothy did in the 90s and my father did in the 80s"

# entity_extraction_module = entity_extractor()
# entities = entity_extraction_module.get_entities(raw_audience_speech)

# print(entities)

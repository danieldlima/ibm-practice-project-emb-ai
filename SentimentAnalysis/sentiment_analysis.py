""" Module providing functionality for working with sentiment using IBM Watson API
"""
import json
import requests

def sentiment_analyzer(text_analyse):
    """ Function to perform sentiment analysis based on text provided as a parameter
    """
    url = ('https://sn-watson-sentiment-bert.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/SentimentPredict')
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    data = {"raw_document": { "text": text_analyse }}

    response = requests.post(url, headers=header, json=data, timeout=10)
    formatted_response = json.loads(response.text)

    label = None
    score = None
    if response.status_code == 200:
        label = formatted_response["documentSentiment"]['label']
        score = formatted_response["documentSentiment"]['score']

    return {'label': label, 'score': score}

""" Module providing functionality for working with sentiment using IBM Watson API
"""
import json
import requests

def emotion_detector(text_analyse):
    """ Function to perform sentiment analysis based on text provided as a parameter
    """
    url = ('https://sn-watson-emotion.labs.skills.network/v1'
           '/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    header = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    data = {'raw_document': { 'text': text_analyse }}

    response = requests.post(url, headers=header, json=data, timeout=10)
    formatted_response = json.loads(response.text)

    label = None
    score = None
    if response.status_code == 200:
        label = formatted_response.get('documentSentiment', {}).get('label')
        score = formatted_response.get('documentSentiment', {}).get('score')

    return {'label': label, 'score': score}

import requests
import json

def sentiment_analyzer(text_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    data = {"raw_document": { "text": text_analyse }}

    response = requests.post(url, headers=header, json=data)
    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    return {'label': label, 'score': score}

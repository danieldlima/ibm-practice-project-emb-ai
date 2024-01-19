import requests
import json

def sentiment_analyzer(text_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    data = {"raw_document": { "text": text_analyse }}

    response = requests.post(url, headers=header, json=data)
    formatted_response = json.loads(response.text)
    document_sentiment = formatted_response["documentSentiment"]
    label = document_sentiment['label'] if response.status_code == 200 else None
    score = document_sentiment['score'] if response.status_code == 200 else None

    return {'label': label, 'score': score}

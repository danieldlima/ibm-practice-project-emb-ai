import requests

def sentiment_analyzer(text_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    data = {"raw_document": { "text": text_analyse }}

    response = requests.post(url, headers=header, json=data)
    return response.text

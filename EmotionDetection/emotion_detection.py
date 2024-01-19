""" Module providing functionality for working with emotion using IBM Watson API
"""
import json

import requests

BASE_URL = ('https://sn-watson-emotion.labs.skills.network/v1'
            '/watson.runtime.nlp.v1/NlpService/EmotionPredict')
HEADERS = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}

def emotion_detector(text_analyse):
    """ Function to perform emotion analysis based on text provided as a parameter
    """
    data = {'raw_document': { 'text': text_analyse }}
    try:
        raw_response = requests.post(BASE_URL, headers=HEADERS, json=data, timeout=10)
        response = json.loads(raw_response.text)

        if raw_response.status_code != 200:
            print(f"[error]: {response.get('message')}")
            return None

        return _process_response(response)
    except requests.exceptions.RequestException as error:
        print(f"[error]: {error}")
        return None

def compose_emotion(response):
    if response is None:
        return None

    dominant_emotion = response['dominant_emotion']
    anger_emotion = response['anger']
    disgust_emotion = response['disgust']
    fear_emotion = response['fear']
    joy_emotion = response['joy']
    sadness_emotion = response['sadness']

    return (f"For the given statement, the system response is "
             f"'anger': {anger_emotion}, 'disgust': {disgust_emotion}, "
             f"'fear': {fear_emotion}, 'joy': {joy_emotion} and "
             f"'sadness': {sadness_emotion}. "
             f"The dominant emotion is {dominant_emotion}.")

def _process_response(response):
    emotion_predictions = response.get('emotionPredictions', {})
    if not emotion_predictions:
        return None

    return _get_emotions_and_dominant(emotion_predictions)

def _get_emotions_and_dominant(emotion_predictions):
    first_prediction = emotion_predictions[0].get('emotion')
    if not first_prediction:
        return None

    emotions = {k: first_prediction.get(k) for k in ['anger', 'disgust', 'fear', 'joy', 'sadness']}
    dominant_emotion = _get_dominant(emotions)
    emotions.update({'dominant_emotion': dominant_emotion})

    return emotions

def _get_dominant(emotions):
    max_emotion_value = max(emotions.values())
    for emotion, value in emotions.items():
        if value == max_emotion_value:
            return emotion.upper()
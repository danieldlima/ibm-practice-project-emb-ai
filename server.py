""" Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
"""
import json

# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, compose_emotion

#Initiate the flask app
app = Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def emotion_analyzer():
    """ This code receives the text from the HTML interface and
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence
        score for the provided text.
    """
    def create_response(res_message, res_status_code, res_data):
        return json.dumps({"message": res_message,
                           "statusCode": res_status_code,
                           "data": res_data}, indent=2), res_status_code

    # Getting 'textToAnalyze' from request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Preparing status message and status code
    message, status_code = (
        ("[error]: No text to analyze was provided", 400)
        if text_to_analyze is None
        else ("success", 200)
    )

    # Constructing Response Data
    response_data = None if text_to_analyze is None else {
        'label': compose_emotion(
            response := emotion_detector(text_to_analyze)
        ),
        'raw_emotion': response
    }

    return create_response(message, status_code, response_data)

@app.route("/")
def render_index_page():
    """ This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template("index.html")

if __name__ == "__main__":
    # his functions execute the flask app and deploys it on localhost:5000
    app.run(debug=True, host="0.0.0.0", port=5000)

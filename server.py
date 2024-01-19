''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
import json

# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Import the sentiment_analyzer function from the package created: TODO

#Initiate the flask app
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """ This code receives the text from the HTML interface and
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence
        score for the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze:
        response = sentiment_analyzer(text_to_analyze)
        label_sentiment = response['label']
        score_sentiment = response['score']
        label = f"The given text has been identified as {label_sentiment.split('_')[0]} with a score of {score_sentiment}"
        data_sentiment = {'label': label, 'score': score_sentiment}
        data_sentiment = {"message": "success", "statusCode": 200, "data": data_sentiment}
        return json.dumps(data_sentiment, indent=2), 200
    else:
        data = {"message": "[error]: No text to analyze was provided", "statusCode": 422, "data": None}
        return json.dumps(data, indent=2), 422

@app.route("/")
def render_index_page():
    """ This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template("index.html")

if __name__ == "__main__":
    """ This functions executes the flask app and deploys it on localhost:5000
    """
    app.run(debug=True, host="0.0.0.0", port=5000)

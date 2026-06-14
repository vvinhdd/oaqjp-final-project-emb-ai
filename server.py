"""
Flask server application for Emotion Detection.
Provides routes to render the user interface and analyze emotions from text.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

APP = Flask(__name__)

@APP.route("/")
def render_index_page():
    """
    Renders the main index.html page for the user interface.
    """
    return render_template('index.html')

@APP.route("/emotionDetector")
def emot_detector():
    """
    Analyzes the input text using emotion_detector and returns a formatted string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    system_response = "For the given statement, the system response is "

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    dynamic_emotions = [(k, v) for k, v in response.items() if k != 'dominant_emotion']
    for i, (key, value) in enumerate(dynamic_emotions):
        score = str(value)
        if i == len(dynamic_emotions) - 1:
            system_response += "and '" + key + "': " + score
        else:
            system_response += "'" + key + "': " + score + ", "

    system_response += ". The dominant emotion is " + response['dominant_emotion'] + "."
    return system_response

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
    
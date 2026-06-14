from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detector():
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


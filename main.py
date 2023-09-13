from predict_sentiment import SentimentPredictor
from translate import SentenceTranslator
from predict_emotion import EmotionPredictor
from flask import Flask, render_template, request

app = Flask(__name__)
translator = SentenceTranslator()
sentiment_predictor = SentimentPredictor()
emotion_predictor = EmotionPredictor()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_sentence = request.form["sentence"]
        translated_sentence = translator.detect_and_translate(input_sentence)
        if isinstance(translated_sentence, tuple):
            result = translated_sentence[-1]
            return render_template("index.html", result=result)
        else:
            sentiment = sentiment_predictor.get_sentiment(translated_sentence)
            sentiment = "Predicted Sentiment: " + sentiment
            emotion = emotion_predictor.get_emotion(translated_sentence)
            emotion = "Emotion: " + emotion.capitalize()
            return render_template("index.html", sentiment=sentiment, emotion=emotion)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
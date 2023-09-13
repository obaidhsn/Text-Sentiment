from predict_sentiment import SentimentPredictor
from translate import SentenceTranslator
from flask import Flask, render_template, request

app = Flask(__name__)
translator = SentenceTranslator()
sentiment_predictor = SentimentPredictor()

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        input_sentence = request.form["sentence"]
        translated_sentence = translator.detect_and_translate(input_sentence)
        if isinstance(translated_sentence, tuple):
            result = translated_sentence[-1]
        else:
            result = sentiment_predictor.get_sentiment(translated_sentence)
            result = "Predicted Sentiment: " + result
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

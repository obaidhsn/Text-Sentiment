# Use a pipeline as a high-level helper
from transformers import pipeline

class EmotionPredictor():
    def __init__(self) -> None:
        self.pipe = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

    def get_emotion(self, sentence):
        emotion = self.pipe(sentence)
        return emotion[0]["label"]

if __name__ == "__main__":
    em = EmotionPredictor()
    print(em.get_emotion("This was one of the greatest Pakistani movies I have ever seen. Well done Sarmad, more power to you."))
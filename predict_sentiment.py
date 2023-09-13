from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


class SentimentPredictor():
    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
        self.model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
        
    def get_sentiment(self, sentence):
        inputs = self.tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            output = self.model(**inputs)

        # Extract the logits tensor
        logits = output.logits

        # If you want the predicted class labels, you can use argmax
        predicted_class_index = logits.argmax().item()

        # If you have access to class labels, you can map the predicted index to a label
        class_labels = ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]
        predicted_class_label = class_labels[predicted_class_index]

        return predicted_class_label
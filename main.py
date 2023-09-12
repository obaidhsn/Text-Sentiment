# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

sentence = "kitna ghatiya insan ha yr ye"

from googletrans import Translator, LANGUAGES

def detect_and_translate(text):
    # Initialize the translator
    translator = Translator()

    # Detect the language of the text
    detected_language = translator.detect(text).lang

    # Translate the text to English
    if detected_language != 'en':
        translation = translator.translate(text, src=detected_language, dest='en').text
    else:
        translation = text  # Text is already in English

    return detected_language, translation

try:
    detected_language, sentence = detect_and_translate(sentence)
except:
    detected_language = None 

print(f"Detected Language: {LANGUAGES.get(detected_language)}")
print(f"Translated Text: {sentence}")


inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
with torch.no_grad():
    output = model(**inputs)

# Extract the logits tensor
logits = output.logits

# If you want the predicted class labels, you can use argmax
predicted_class_index = logits.argmax().item()

# If you want the probability scores for each class, you can apply softmax
softmax_scores = torch.softmax(logits, dim=1)
predicted_probabilities = softmax_scores[0].tolist()  # Assuming a batch size of 1

# If you have access to class labels, you can map the predicted index to a label
class_labels = ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]
predicted_class_label = class_labels[predicted_class_index]

# Print the results
print("Predicted Class Label:", predicted_class_label)




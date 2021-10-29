import csv
from google.cloud import language_v1

client = language_v1.LanguageServiceClient()

with open('test.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[2] for row in reader]

for key in column:
    text = column[key]
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    print("Text: {}".format(text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))


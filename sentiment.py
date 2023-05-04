from textblob import TextBlob
import re

def analyze_text(text):

    sentiment_polarity_sum = 0
    sentiment_subjectivity_sum = 0
    num_phrases = 0
    positive_statements = []
    negative_statements = []
    neutral_statements = []
 
    phrases = re.findall(r'[^.?!\n]+[.?!\n]', text)

    with open("sentiment_report.txt", "w") as file:
        file.write("")

    with open("Statements.txt", "w") as file:
        file.write("")
    
    for phrase in phrases:
        # Perform sentiment analysis on the phrase using TextBlob
        analysis = TextBlob(phrase)

        # Print the sentiment polarity and subjectivity for the phrase
        # print(f"Phrase: {phrase.strip()}")
        # print(f"Sentiment polarity: {analysis.sentiment.polarity}")

        if analysis.sentiment.polarity>0:
            nature = 'POSITIVE'
            positive_statements.append(phrase.strip())
        elif analysis.sentiment.polarity<0:
            nature = 'NEGATIVE'
            negative_statements.append(phrase.strip())
        else:
            nature = 'NEUTRAL'
            neutral_statements.append(phrase.strip())

        with open("sentiment_report.txt", "a") as file:
            file.write(f"Phrase: {phrase.strip()}\n")
            file.write(f"Sentiment polarity: {analysis.sentiment.polarity}\n")
            file.write(f"Sentiment nature: {nature}\n")
            file.write(f"Sentiment subjectivity: {analysis.sentiment.subjectivity}\n")
            file.write("\n")
                
        # Add the sentiment scores to the running total
        sentiment_polarity_sum += analysis.sentiment.polarity
        sentiment_subjectivity_sum += analysis.sentiment.subjectivity
        num_phrases += 1

    # Calculate the overall sentiment polarity and subjectivity for the entire text
    overall_sentiment_polarity = sentiment_polarity_sum / num_phrases
    overall_sentiment_subjectivity = sentiment_subjectivity_sum / num_phrases

    with open("Statements.txt", "a") as file:

        file.write("POSITIVE STATEMENTS MADE : \n")
        file.write("\n")
        for idx,i in enumerate(positive_statements):
            file.write(str(idx+1)+'. '+i)
            file.write("\n")

        file.write("\n")
        file.write("NEGATIVE STATEMENTS MADE : \n")
        file.write("\n")
        for idx,i in enumerate(negative_statements):
            file.write(str(idx+1)+'. '+i)
            file.write("\n")

        file.write("\n")
        file.write("NEUTRAL STATEMENTS MADE : \n")
        file.write("\n")
        for idx,i in enumerate(neutral_statements):
            file.write(str(idx+1)+'. '+i)
            file.write("\n")

    # Print the overall sentiment polarity and subjectivity for the entire text
    print(f"Overall sentiment polarity: {overall_sentiment_polarity}")
    print(f"Overall sentiment subjectivity: {overall_sentiment_subjectivity}")


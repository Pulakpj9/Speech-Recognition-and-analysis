import spacy
from spacy.lang.en.stop_words import STOP_WORDS
# from string import punctuation
# Now we are going to select 30% of the sentences having the largest scores. For this we are going to import nlargest from heapq.
from heapq import nlargest

def summarize_text(txt):
    # creating the list of stop words
    stopwords = list(STOP_WORDS)
    # print(stopwords)

    #spacy.load is used to load a model. spacy.load('en_core_web_sm') loads the model package en_core_web_sm. This will return a language object nlp containing all components and data needed to process text.
    nlp = spacy.load('en_core_web_sm')

    # Calling the nlp object on a string of text will return a processed Doc. During processing, spaCy first tokenizes the text, i.e. segments it into words, punctuation and so on.
    doc = nlp(txt)

    # Each Doc consists of individual tokens, and we can iterate over them. Now we will make a list of tokens called tokens.
    tokens = [token.text for token in doc]
    # print(tokens)

    #We can see that all the punctuation marks and special characters are included in the tokens. Now we will remove them. punctuation contains a string of all the punctuations but it does now conatin \n. So we will add \n in punctuation.
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    punctuation = punctuation + '\n'
    # print(punctuation)

    # Now we will make the word frequency table. It will contain the number of occurrences of all the distinct words in the text which are not punctuations or stop words. We will create a dictionary named word_frequencies.

    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
                    
    # print(word_frequencies)

    #Now we will get the max_frequency.

    max_frequency = max(word_frequencies.values())
    # print(max_frequency)

    # We will divide each frequency value in word_frequencies with the max_frequency to normalize the frequencies.

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    # print(word_frequencies)

    # Now we will do sentence tokenization. The entire text is divided into sentences.

    sentence_tokens = [sent for sent in doc.sents]
    # print(sentence_tokens)

    # Now we will calculate the sentence scores. The sentence score for a particular sentence is the sum of the normalized frequencies of the words in that sentence. All the sentences will be stored with their score in the dictionary sentence_scores.

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
                    
    # sentence_scores

    # We want the length of summary to be 30% of the original length which is 4. Hence the summary will have 4 sentences.

    select_length = int(len(sentence_tokens)*0.3)
    # print(select_length)

    #nlargest() will return a list with the select_length largest elements i.e. 4 largest elements from sentence_scores. key = sentence_scores.get specifies a function of one argument that is used to extract a comparison key from each element in sentence_scores.

    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
    # print(summary)

    # Now we will combine this sentence together and make final string which contains the summary.

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    with open("summary.txt", "w") as file:
        file.write("")
    
    with open("summary.txt", "a") as file:
            file.write(summary)
    # print(summary)
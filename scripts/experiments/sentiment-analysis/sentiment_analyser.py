from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import classify, NaiveBayesClassifier
import re, string

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)
        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

def create_dataset(file1, file2, file3, stop_words):
    positive_tweet_tokens = []
    negative_tweet_tokens = []
    neutral_tweet_tokens = []
    r = open("" + str(file1) + "" ,"r")
    for line in r:
        token = word_tokenize(line)
        positive_tweet_tokens.append(token)
    r = open("" + str(file2) + "","r")
    for line in r:
        token = word_tokenize(line)
        negative_tweet_tokens.append(token)
    r = open("" + str(file3) + "","r")
    for line in r:
        token = word_tokenize(line)
        neutral_tweet_tokens.append(token)

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []
    neutral_cleaned_tokens_list = []

    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in neutral_tweet_tokens:
        neutral_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)
    neutral_tokens_for_model = get_tweets_for_model(neutral_cleaned_tokens_list)

    positive_dataset = [(tweet_dict, "Positive")
                         for tweet_dict in positive_tokens_for_model]

    negative_dataset = [(tweet_dict, "Negative")
                         for tweet_dict in negative_tokens_for_model]

    neutral_dataset = [(tweet_dict, "Neutral")
                         for tweet_dict in neutral_tokens_for_model]

    dataset = positive_dataset + negative_dataset + neutral_dataset

    return dataset

if __name__ == "__main__":
    stop_words = []
    r = open("lv_stopwords.txt","r")
    for line in r:
        stop_words.append(line.replace('\n',''))

    testing_set = create_dataset("experiment-data/test.pos","experiment-data/test.neg", "experiment-data/test.nei", stop_words)
    training_set = create_dataset("experiment-data/train.pos","experiment-data/train.neg", "experiment-data/train.nei", stop_words)

    classifier = NaiveBayesClassifier.train(training_set)

    print("Accuracy is:", classify.accuracy(classifier, testing_set))

    print(classifier.show_most_informative_features(10))

    custom_tweet = "Šodien pusdienās ēdīšu pasūtījumu no Wolt."

    custom_tokens = remove_noise(word_tokenize(custom_tweet))

    print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
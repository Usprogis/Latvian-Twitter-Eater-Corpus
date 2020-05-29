# Latvian-Twitter-Eater-Corpus

This repo contains valuable information about the Latvian Twitter Eater Corpus.
The structure is like this:
- scripts
- text
- twitter-eater-corpus


## scripts
This repo contains script files writen in Python, used to gather information from the Latvian Twitter Eater Corpus or LTEC for short.
Here's a short summary about each of them:
- data_converter.py - converts the tweet data from the MYSQL database to JSON format file.
- filewriter.py - writes all JSON file content in one JSON file.
- years_months.py - gets tweet count for each year and month and visualise it into a graph.
- top_food_overall.py - gets information about the most used food and drink words mentioned in tweets.
- sentiment_analyser.py - takes as input tweet text files labeled as positive, negative and neutral, and returns the accuracy of the
developed sentiment analyser.

## text
The repo also contains subgroups of tweets such as a group of tweets representing questions and replies gathered from the Twitter API.
A group of tweets containing positive and negative emoticons and group of tweets used to train and test a selfmade sentiment analyser.
They are labeled as:
- full_replies.json - questions and replies tweets.
- bad_emoji_count.txt - bad emoticon tweets.
- good_emoji_count.txt - good emoticon tweets.
- train_pos, train_neg, train_nei - tweet data used to train the sentiment analyser.
- test_pos.txt, test_neg.txt, test_nei.txt - tweet data used to evaluate the sentiment analyser.
- lv_stopwords.txt - latvian stopwords used in the sentiment analyser.

## twitter-eater-corpus
This folder contains the LTEC. All information from the corpus is hidden, and only the tweet ID are available due to Twitter data usage
rights. To gain the full corpus information, please, contact the repos owner.

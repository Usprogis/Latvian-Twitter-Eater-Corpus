# Latvian Twitter Eater Corpus

This repository contains the Latvian Twitter Eater Corpus.
Repository structure:
- **full-corpus** - the full corpus in several formats
- **sub-corpora** - task-specific sub-corpora derrived from th full corpus
- **scripts** - scripts for data preparation and analyis


Scripts
---------
This directory contains script files writen in Python, used to gather information from the Latvian Twitter Eater Corpus or LTEC for short.
Here's a short summary about each of them:
- **data_converter.py** - converts the tweet data from the MYSQL database to JSON format file.
- **filewriter.py** - writes all JSON file content in one JSON file.
- **years_months.py** - gets tweet count for each year and month and visualise it into a graph.
- **top_food_overall.py** - gets information about the most used food and drink words mentioned in tweets.
- **sentiment_analyser.py** - takes as input tweet text files labeled as positive, negative and neutral, and returns the accuracy of the
developed sentiment analyser.
- **lv_stopwords.txt** - latvian stopwords used in the sentiment analyser.

Sub-corpora
---------
The directory contains sub-corpora of tweets such as a tweets representing questions and replies gathered from the Twitter API.
A group of tweets containing positive and negative emoticons, tweets who authors are the latvian media and restaurant accounts  and group of tweets used to train and test a selfmade sentiment analyser.
They are labeled as:
- **ltec-questions-answers.json** - tweet data that contains answer data to a question tweet.
- **ltec-answers-questions.json** - tweet data that contains question data. 
- **ltec-sentiment-annotated.json** - contains tweets with human annotated sentiment where each tweet represented as in the tweet structure.
- **ltec-sentiment-automatic.json** contains tweets with automatically assigned sentiment based on emoticons.

Full-corpus
---------
This directory contains the LTEC. All information from the corpus is hidden, and only the tweet ID are available due to Twitter data usage
rights. To gain the full corpus information, please, contact the repos owner.


Publications
---------

If you use this corpus or scripts, please cite the following paper:

Uga Sproģis and Matīss Rikters (2020). "[What Can We Learn From Almost a Decade of Food Tweets.](https://klc.vdu.lt/hlt/programme)" In Proceedings of the 9th Conference Human Language Technologies - The Baltic Perspective (Baltic HLT 2020) (2020).

```bibtex
@inproceedings{SprogisRikters2020BalticHLT,
	author = {Sproģis, Uga and Rikters, Matīss},
	booktitle={In Proceedings of the 9th Conference Human Language Technologies - The Baltic Perspective (Baltic HLT 2020)},
	title = {{What Can We Learn From Almost a Decade of Food Tweets}},
	address={Kaunas, Lithuania},
	year = {2020}
}
```

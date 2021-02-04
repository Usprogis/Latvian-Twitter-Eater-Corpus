# Sentiment Analysis Sub-corpus

This sub-corpus contains 5420 tweets with human-annotated sentiment as positive (pos), neutral (neu) or negative (neg). 1631 tweets are positive, 2507 - neutral and 1282 - negative.

- **ltec-sentiment-annotated.json** contains tweets with human annotated sentiment
- **ltec-sentiment-annotated-test.json** contains the test set that we used in our paper
- **ltec-sentiment-automatic.json** contains tweets with automatically assigned sentiment based on emoticons

## Tweet Structure
```json
{   
	"sentiment":"pos",
	"screen_name":"artisare",
	"tweet_id":221520985738846209,
	"tweet_text":"@mazheks Burgā ir brančs?!? Es jau sāku domāt ka uz Pērli jāmauc ēst pirms tam Illy paķerot kafiju. Cikos domā?"
}
```


## Other Latvian twitter sentiment corpora
---------
* [Pinnis](https://github.com/pmarcis/latvian-tweet-corpus) - ~ 7000 tweets from politicians and companies
* [Peisenieks](https://github.com/FnTm/latvian-tweet-sentiment-corpus) - ~ 1000 general tweets with sentiment annotated by multiple annotators
* [Vīksna](https://github.com/RinaldsViksna/sikzinu_analize) - ~ 4000 general tweets
* [Nicmanis](https://github.com/nicemanis/LV-twitter-sentiment-corpus) - ~ 2000 general tweets
* [Špats](https://github.com/gatis/om) - ~ 6000 general tweets (lowercased)
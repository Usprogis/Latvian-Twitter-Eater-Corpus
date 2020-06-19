# Sentiment Analysis Sub-corpus
- questions-answers.json contains tweets in the following format where each entry contains a tweet id, text, author and
one or more answers with id, text, author for each answer

```json
{   
	"answers":[
		{
			"a_screen_name":"mazheks",
			"a_tweet_id":221521408478560256,
			"a_tweet_text":"tagad esam ceļā uz turieni"
		},
		{
			"a_screen_name":"artisare",
			"a_tweet_id":221526513579851778,
			"a_tweet_text":"oki doki. Rezervē vietu pie galdiņa."
		},
		{
			"a_screen_name":"mazheks",
			"a_tweet_id":221521278463516672,
			"a_tweet_text":"burgā ir lieliskas omletes"
		}   
	],
	"q_screen_name":"artisare",
	"q_tweet_id":221520985738846209,
	"q_tweet_text":"@mazheks Burgā ir brančs?!? Es jau sāku domāt ka uz Pērli jāmauc ēst pirms tam Illy paķerot kafiju. Cikos domā?"
}
```


Other Latvian twitter sentiment corpora
---------
* [Pinnis](https://github.com/pmarcis/latvian-tweet-corpus) - ~ 7000 tweets from politicians and companies
* [Peisenieks](https://github.com/FnTm/latvian-tweet-sentiment-corpus) - ~ 1000 general tweets with sentiment annotated by multiple annotators
* [Vīksna](https://github.com/RinaldsViksna/sikzinu_analize) - ~ 4000 general tweets
* [Nicmanis](https://github.com/nicemanis/LV-twitter-sentiment-corpus) - ~ 2000 general tweets
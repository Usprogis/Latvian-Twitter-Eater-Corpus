# Question-answer Sub-corpus
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

- answers-questions.json contains question tweets that were replies to other tweets along with the tweets they replied to. In this case 
`reply_id`, `reply_author`, `reply_text` corresponds to a tweet and `question_id`, `question_author`, `question_text` is the answer to that tweet. 

```json
{
	"question_id":  122043032949366784,
	"question_author":  "linda_dzirniece",
	"question_text":  "@lelde_krukle paldies, tev par tām gardajām biezpienbulciņām! kā tev vakar garšoja burgers? ;)",
	"reply_id":  122037974522277888,
	"reply_author":  "lelde_krukle",
	"reply_text":  "še jums, bulciņu rijēji. http://t.co/guPddwD5",
}
```
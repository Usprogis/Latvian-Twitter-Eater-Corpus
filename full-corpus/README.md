# Latvian Twitter Eater Corpus
This repository contains the publishable part of the Latvian Twitter Eater Corpus and a set of tools/scripts to work with it.
A simple analysis of the last few months worth of these tweets can always be found in the [TwitĒdiens](http://twitediens.ml/) website.

# Files
- **ltec-full-tweet-ids.txt** contains IDs of all tweets from the corpus - one per line. A quick way to get tweets (and replies) using IDs is [scraping Twitters website](https://github.com/M4t1ss/TwEater)
- **ltec-full.json** contains the full version of the corpus with each tweet represented as in the [tweet structure](#tweet-structure). 
	- All tweets have at least the following properties: `tweet_id`, `tweet_text`, `tweet_author`, `created_at`. 
	- The remaining properties are optional - `location_` properties are only for tweets that had location information and `food_` properties are only for tweets which mention at least one food/drink.
	- Each consecutive food/drink in the `food_` properties is separated using a semicolon.
	- Food groups are according to the food guide pyramid: bread, cereal, rice, pasta (6); vegetables (5); fruit, berries (4); milk products (3); meat, eggs, fish (2); fats, oils, sweets (1). We added two more groups for alcoholic drinks (7) and non-alcoholic drinks (8).

# Tweet Structure
```json
{
	"tweet_id":  1213025400273735680,
	"tweet_text":  "Gulašzupa #receptesĪsumā gulašzupa ir gana vienkārša liellopu gaļas bāzēta zupa https://t.co/OnqDwotQr0 https://t.co/Z2tAodyj9M",
	"tweet_author":  "receptes_eu",
	"created_at":  "2020-01-03 11:12:54",
	"media_url":  "http://pbs.twimg.com/media/ENWIKb8WsAAiLKE.jpg",
	"expanded_url":  "https://twitter.com/receptes_eu/status/1213025400273735680/photo/1",
	"location_name":  "Ogresgals",
	"location_lng":  "24.7377",
	"location_lat":  "56.8079",
	"location_country":  "Latvia",
	"food_surface_form":  "Gulašzupa;liellopu;gaļas;zupa;",
	"food_nominative_form":  "gulašs;liellops;gaļa;zupa;",
	"food_group":  "2;2;2;6;",
	"food_english_translation":  "Goulash;Cattle;Meat;Soup;",
}
```
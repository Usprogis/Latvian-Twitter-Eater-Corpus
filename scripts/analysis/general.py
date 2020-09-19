import ijson
from collections import Counter

def get_field_data(search_field):
	file = open("ltec-full.json", 'rb')
	objects = ijson.items(file, search_field)
	data = list(objects)
	file.close()
	return data

print("Overall statitics of the LTEC:")
tweet_count = len(get_field_data("item.tweet_id"))
print("\t" + "Corpus contains " + str(tweet_count) + " tweets.")
media_tweet_count = len(get_field_data("item.media_url"))
print("\t" + str(media_tweet_count) + " or " + str("{:0.2f}".format(media_tweet_count * 100 / tweet_count)) + "% of tweets contain media information.")
location_tweet_count = len(get_field_data("item.location_name"))
print("\t" + str(location_tweet_count) + " or " + str("{:0.2f}".format(location_tweet_count * 100 / tweet_count)) + "% of tweets contain place information.")
food_tweet_count = len(get_field_data("item.food_surface_form"))
print("\t" + str(food_tweet_count) + " or " + str("{:0.2f}".format(food_tweet_count * 100 / tweet_count)) + "% of tweets contain food information.\n")

print("Overall year statitics:")
year = 2011
count = 0
tweets_over_years = get_field_data("item.created_at")
for year_tweet in tweets_over_years:
	if year_tweet.find(str(year)) == -1:
		print("\t" + str(year) + " had " + str(count) + " tweets.")
		year += 1
		count = 0
	else:
		count += 1
print("\t" + str(year) + " had " + str(count) + " tweets." + "\n")

print("Most mentioned foods and drinks:")
food_data = get_field_data("item.food_nominative_form")
food_list = []
for unit in food_data:
	temp_food_list = unit[:-1].split(";")
	food_list.extend(temp_food_list)
top_foods = Counter(food_list)
top = top_foods.most_common(10)
for food in top:
	print("\tFood name:" + str(food[0]) + " and count: " + str(food[1]))
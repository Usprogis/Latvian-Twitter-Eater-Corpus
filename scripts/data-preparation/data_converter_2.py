import mysql.connector as mysql
import sys,json

"""
create table tweets1 as select * from tweets left join media on tweets.id = media.tweet_id;
create table tweets2 as select * from tweets1 left join vietas on tweets1.geo = vietas.nosaukums;
ALTER TABLE tweets2 ORDER BY created_at ASC;
create table tweets3 as select * from tweets2 t left join (SELECT distinct(tvits) FROM words o) AS o ON o.tvits = t.id;
"""


db = mysql.connect(user='root', password='root',host='localhost',database='july_import', port='3306')
mycursor = db.cursor()

db1 = mysql.connect(user='root', password='root',host='localhost',database='july_import', port='3306')
mycursor1 = db1.cursor()

if len(sys.argv) > 1 and sys.argv[1] > 2010 and sys.argv[1] < 2021:
    print(sys.argv[1])
    mycursor.execute("SELECT * FROM tweets3 where YEAR(created_at) = '"+sys.argv[1]+"'")
else:
    mycursor.execute("SELECT id, text, screen_name, created_at, media_url, expanded_url, nosaukums, lng, lat, valsts FROM tweets3")

x = open("tweets_latest.json", "w")
x.write("[\n")

for results in mycursor:

    tweet_dict = {}
    
    if str(results[4]) != "None":
        tweet_dict["media_url"] = str(results[4])
    if str(results[5]) != "None":
        tweet_dict["expanded_url"] = str(results[5])
    if str(results[6]) != "None":
        tweet_dict["location_name"] = str(results[6])
    if str(results[7]) != "None":
        tweet_dict["location_lng"] = str(results[7])
    if str(results[8]) != "None":
        tweet_dict["location_lat"] = str(results[8])
    if str(results[9]) != "None":
        tweet_dict["location_country"] = str(results[9])
    
    fsfp = ""
    fnfp = ""
    fgp = ""
    fetp = ""
    fsf = ""
    fnf = ""
    fg = ""
    fet = ""
    
    search = (results[0],)
    sql = "select * from words where tvits = %s"
    mycursor1.execute(sql,search);
    res = mycursor1.fetchall()
    
    if str(res) != "None" and res != []:
        for r in res:
            fsfp += str(r[0]) + ";"
            fnfp += str(r[1]) + ";"
            fgp += str(r[4]) + ";"
            fetp += str(r[5]) + ";"

        tweet_dict["food_surface_form"] = fsfp
        tweet_dict["food_nominative_form"] = fnfp
        tweet_dict["food_group"] = fgp
        tweet_dict["food_english_translation"] = fetp
       
    #Write everything only once.
    tweet_dict["tweet_id"] = str(results[0])
    tweet_dict["tweet_text"] = str(results[1]).replace("\n","")
    tweet_dict["tweet_author"] = str(results[2])
    tweet_dict["created_at"] = str(results[3])
    
    output = json.dumps(tweet_dict, sort_keys=True, ensure_ascii=False)
    
    x.write(output.strip() + ",\n")

x.write("]")

x.close()

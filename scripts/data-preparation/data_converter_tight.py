import mysql.connector as mysql
import sys
from datetime import date

db = mysql.connect(user='root', password='root',host='localhost',database='twitter', port='3306')
mycursor = db.cursor()

gads = ""
tagad = date.today().year + 1
if len(sys.argv) > 1 and int(sys.argv[1]) > 2010 and int(sys.argv[1]) < int(tagad):
    gads = sys.argv[1]
    print(gads)
    mycursor.execute("SELECT id, text, screen_name, created_at, media_url, expanded_url, nosaukums, lng, lat, valsts, vards, nominativs, grupa, eng FROM tweets4 where YEAR(created_at) = '"+gads+"'")
else:
    mycursor.execute("SELECT id, text, screen_name, created_at, media_url, expanded_url, nosaukums, lng, lat, valsts, vards, nominativs, grupa, eng FROM tweets4")

x = open("tweets_"+gads+".json", "w")
cot = 1

for results in mycursor:

    fsfp = ""
    fnfp = ""
    fgp = ""
    fetp = ""
    fsf = ""
    fnf = ""
    fg = ""
    fet = ""
    media = ""
    url = ""
    locn = ""
    loclg = ""
    loclt = ""
    locc = ""
    
    if str(results[4]) != "None":
        media = " " + ", \"media_url\": " + "\"" + str(results[4]) + "\""
    if str(results[5]) != "None":
        url = " " + ", \"expanded_url\": " + "\"" + str(results[5]) + "\""
    if str(results[6]) != "None":
        locn = " " + ", \"location_name\": " + "\"" + str(results[6]) + "\""
    if str(results[7]) != "None":
        loclg = " " + ", \"location_lng\": " + "\"" + str(results[7]) + "\""
    if str(results[8]) != "None":
        loclt = " " + ", \"location_lat\": " + "\"" + str(results[8]) + "\""
    if str(results[9]) != "None":
        locc = " " + ", \"location_country\": " + "\"" + str(results[9]) + "\""
    
    if str(results[10]) != "None":
        fsf = ", \"food_surface_form\": " + "\"" + str(results[10]) + "\""
        fnf = ", \"food_nominative_form\": " + "\"" + str(results[11]) + "\""
        fg = ", \"food_group\": " + "\"" + str(results[12]) + "\""
        fet = ", \"food_english_translation\": " + "\"" + str(results[13]) + "\""
       
    #Write everything only once.
    #Tight
    x.write("    {" + "\"created_at\": " + "\"" + str(results[3]) + "\"" + ", " + "\"tweet_id\": " + str(results[0]) + ", " + "\"tweet_text\": " + "\"" 
        + str(results[1]).replace('"', '\\"').replace("\n","") + "\"" + ", " + "\"tweet_author\": " + "\"" + str(results[2]) + "\"" 
        + media + url + locn + loclg 
        + loclt + locc + fsf + fnf + fg + fet + "},\n")
    cot += 1

x.close()
print("Done!")
print(cot)

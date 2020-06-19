import mysql.connector as mysql

db = mysql.connect(user='root', password='root',host='localhost',database='twitter')

mycursor = db.cursor()

mycursor.execute("SELECT * FROM tweets2013Q1")

x = open("tweets2013Q1.json", "w")
cot = 1
x.write("[\n")

results = mycursor.fetchone()
while results != None:
	x.write("    {\n")
	x.write("      " + "\"tweet_id\":  " + str(results[0]) + ",\n")
	x.write("      " + "\"tweet_text\":  " + "\"" + str(results[1]).replace("\n","") + "\"" + ",\n")
	x.write("      " + "\"tweet_author\":  " + "\"" + str(results[2]) + "\"" + ",\n")
	x.write("      " + "\"created_at\":  " + "\"" + str(results[3]) + "\"" + ",\n")
	if str(results[7]) == "None":
		x.write("      " + "\"media_url\":  " + "\"""\"" + ",\n")
	else:
		x.write("      " + "\"media_url\":  " + "\"" + str(results[7]) + "\"" + ",\n")
	if str(results[8]) == "None":
		x.write("      " + "\"expanded_url\":  " + "\"""\"" + ",\n")
	else:
		x.write("      " + "\"expanded_url\":  " + "\"" + str(results[8]) + "\"" + ",\n")
	if str(results[10]) == "None":
		x.write("      " + "\"location_name\":  " + "\"""\"" + ",\n")
	else:
		x.write("      " + "\"location_name\":  " + "\"" + str(results[10]) + "\"" + ",\n")
	if str(results[11]) == "None":
		x.write("      " + "\"location_lng\":  " + "\"""\"" + ",\n")
	else:
		x.write("      " + "\"location_lng\":  " + "\"" + str(results[11]) + "\"" + ",\n")
	if str(results[12]) == "None":
		x.write("      " + "\"location_lat\":  " + "\"""\"" + ",\n")
	else:
		x.write("      " + "\"location_lat\":  " + "\"" + str(results[12]) + "\"" + ",\n")
	if str(results[13]) == "None":
		x.write("      " + "\"location_country\":  " + "\"""\"" + ",\n")
	else:
		x.write("      " + "\"location_country\":  " + "\"" + str(results[13]) + "\"" + ",\n")



	db1 = mysql.connect(user='root', password='root',host='localhost',database='twitter')
	mycursor1 = db1.cursor()
	search = (results[0],)
	sql = "select * from words2013Q1 where tvits = %s"
	mycursor1.execute(sql,search);
	res = mycursor1.fetchall()

	if str(res) == "None" or res == []:
		x.write("      " + "\"food_surface_form\":  " + "\"""\"" + ",\n")
	else:
		x.write("      " + "\"food_surface_form\":  " + "\"")
		for r in res:
			x.write(str(r[0]) + ";")
		x.write("\"" + ",\n")

	if str(res) == "None" or res == []:
		x.write("      " + "\"food_nominative_form\":  " + "\"""\"" + ",\n")
	else:
		x.write("      " + "\"food_nominative_form\":  " + "\"")
		for r in res:
			x.write(str(r[1]) + ";")
		x.write("\"" + ",\n")

	if str(res) == "None" or res == []:
		x.write("      " + "\"food_group\":  " + "\"""\"" + ",\n")
	else:
		x.write("      " + "\"food_group\":  " + "\"")
		for r in res:
			x.write(str(r[4]) + ";")
		x.write("\"" + ",\n")

	if str(res) == "None" or res == []:
		x.write("      " + "\"food_english_translation\":  " + "\"""\"" + ",\n")
	else:
		x.write("      " + "\"food_english_translation\":  " + "\"")
		for r in res:
			x.write(str(r[5]) + ";")
		x.write("\"" + ",\n")	
	x.write("    },\n")
	print(cot)
	cot = cot + 1

x.write("]")

x.close()
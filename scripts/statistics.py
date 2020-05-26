import mysql.connector as mysql

db = mysql.connect(user='root', password='root',host='localhost',database='twitter')

mycursor = db.cursor()

sum = 0
cot = 0
"""
f = open("mediji.txt", "r")
for x in f:
	y = "" + str(x.replace('\n','')) + ""
	args = (y,)
	query = "SELECT count(*) FROM tweets where screen_name = %s"
	mycursor.execute(query,args)
	result = mycursor.fetchall()
	sum += result[0][0]
	cot += 1
	print(cot)
f.close()
print(sum)
"""
r = open("newData_count.txt", "w")
f = open("newData.txt", "r")
for x in f:
	y = "" + str(x.replace('\n','')) + ""
	args = (y,)
	query = "SELECT text FROM tweets where screen_name = %s"
	mycursor.execute(query,args)
	results = mycursor.fetchone()
	while results != None:
		r.write(results[0].replace("\n","") + "\n")
		results = mycursor.fetchone()
	cot +=1
	print(cot)
f.close()
r.close()

"""
sum = 0
cot = 0

f = open("restorani.txt", "r")
for x in f:
	y = "" + str(x.replace('\n','')) + ""
	args = (y,)
	query = "SELECT count(*) FROM tweets where screen_name = %s"
	mycursor.execute(query,args)
	result = mycursor.fetchall()
	sum += result[0][0]
	cot += 1
	print(cot)
f.close()

r = open("restorani_count.txt", "w")
f = open("restorani.txt", "r")
for x in f:
	y = "" + str(x.replace('\n','')) + ""
	args = (y,)
	query = "SELECT text FROM tweets where screen_name = %s"
	mycursor.execute(query,args)
	results = mycursor.fetchone()
	while results != None:
		r.write(results[0].replace("\n","") + "\n")
		results = mycursor.fetchone()
	cot +=1
	print(cot)
f.close()
r.close()
print(sum)
"""
import mysql.connector as mysql
from pandas import DataFrame
import matplotlib.pyplot as plt

db = mysql.connect(user='root', password='root',host='localhost',database='twitter')

mycursor = db.cursor()

years = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

year = 2011
y = 0
month = 1
cot = 0
sum = 0
ty = []

while cot < 120:
	if month % 13 == 0:
		month = 1
		year += 1
		y +=1
	args = (year,month,)
	query = "SELECT count(*) FROM tweets  WHERE YEAR(created_at) = %s and MONTH(created_at) = %s"
	mycursor.execute(query,args)
	results = mycursor.fetchall()
	years[y][month-1] = results[0][0]
	cot += 1
	month += 1
	print(years)

Data = {'Tvītu skaits': [years[0][0],years[0][1],years[0][2],years[0][3],years[0][4],years[0][5],years[0][6],years[0][7],years[0][8],years[0][9],years[0][10],years[0][11],years[1][0],years[1][1],years[1][2],years[1][3],years[1][4],years[1][5],years[1][6],years[1][7],years[1][8],years[1][9],years[1][10],years[1][11],years[2][0],years[2][1],years[2][2],years[2][3],years[2][4],years[2][5],years[2][6],years[2][7],years[2][8],years[2][9],years[2][10],years[2][11],years[3][0],years[3][1],years[3][2],years[3][3],years[3][4],years[3][5],years[3][6],years[3][7],years[3][8],years[3][9],years[3][10],years[3][11],years[4][0],years[4][1],years[4][2],years[4][3],years[4][4],years[4][5],years[4][6],years[4][7],years[4][8],years[4][9],years[4][10],years[4][11],years[5][0],years[5][1],years[5][2],years[5][3],years[5][4],years[5][5],years[5][6],years[5][7],years[5][8],years[5][9],years[5][10],years[5][11],years[6][0],years[6][1],years[6][2],years[6][3],years[6][4],years[6][5],years[6][6],years[6][7],years[6][8],years[6][9],years[6][10],years[6][11],years[7][0],years[7][1],years[7][2],years[7][3],years[7][4],years[7][5],years[7][6],years[7][7],years[7][8],years[7][9],years[7][10],years[7][11],years[8][0],years[8][1],years[8][2],years[8][3],years[8][4],years[8][5],years[8][6],years[8][7],years[8][8],years[8][9],years[8][10],years[8][11],years[9][0],years[9][1],years[9][2],years[9][3],years[9][4],years[9][5],years[9][6],years[9][7],years[9][8],years[9][9],years[9][10],years[9][11]],
        'Gads_mēnesis': ["2011-01","2011-02","2011-03","2011-04","2011-05","2011-06","2011-07","2011-08","2011-09","2011-10","2011-11","2011-12","2012-01","2012-02","2012-03","2012-04","2012-05","2012-06","2012-07","2012-08","2012-09","2012-10","2012-11","2012-12","2013-01","2013-02","2013-03","2013-04","2013-05","2013-06","2013-07","2013-08","2013-09","2013-10","2013-11","2013-12","2014-01","2014-02","2014-03","2014-04","2014-05","2014-06","2014-07","2014-08","2014-09","2014-10","2014-11","2014-12","2015-01","2015-02","2015-03","2015-04","2015-05","2015-06","2015-07","2015-08","2015-09","2015-10","2015-11","2015-12","2016-01","2016-02","2016-03","2016-04","2016-05","2016-06","2016-07","2016-08","2016-09","2016-10","2016-11","2016-12","2017-01","2017-02","2017-03","2017-04","2017-05","2017-06","2017-07","2017-08","2017-09","2017-10","2017-11","2017-12","2018-01","2018-02","2018-03","2018-04","2018-05","2018-06","2018-07","2018-08","2018-09","2018-10","2018-11","2018-12","2019-01","2019-02","2019-03","2019-04","2019-05","2019-06","2019-07","2019-08","2019-09","2019-10","2019-11","2019-12","2020-01","2020-02","2020-03","2020-04","2020-05","2020-06","2020-07","2020-08","2020-09","2020-10","2020-11","2020-12"]
       }
  
df = DataFrame(Data,columns=['Tvītu skaits','Gads_mēnesis'])
df.plot(x ='Gads_mēnesis', y='Tvītu skaits', kind = 'bar')
plt.show()


year = 2011
while year < 2021:
	args = (year,)
	query = "SELECT count(*) FROM tweets  WHERE YEAR(created_at) = %s"
	mycursor.execute(query,args)
	results = mycursor.fetchall()
	sum = results[0][0]
	ty.append(sum)
	year +=1
	print(ty)



Data = {'Tvītu skaits': [ty[0],ty[1],ty[2],ty[3],ty[4],ty[5],ty[6],ty[7],ty[8],ty[9]],
        'Gads': [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
       }
  
df = DataFrame(Data,columns=['Tvītu skaits','Gads'])
df.plot(x ='Gads', y='Tvītu skaits', kind = 'bar')
plt.show()

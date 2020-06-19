import mysql.connector as mysql
from pandas import DataFrame
import matplotlib.pyplot as plt

db = mysql.connect(user='root', password='root',host='localhost',database='twitter')

mycursor = db.cursor()

mycursor.execute("select nominativs,count(*) from words where grupa = 1 OR grupa = 2 OR grupa = 3 OR grupa = 4 or grupa = 5 or grupa = 6 group by nominativs order by count(nominativs) desc limit 10")

results = mycursor.fetchall()

Data = {'Reizes pieminēts': [results[0][1],results[1][1],results[2][1],results[3][1],results[4][1],results[5][1],results[6][1],results[7][1],results[8][1],results[9][1]],
        'Ēdieni': [results[0][0],results[1][0],results[2][0],results[3][0],results[4][0],results[5][0],results[6][0],results[7][0],results[8][0],results[9][0]]
       }
  
df = DataFrame(Data,columns=['Reizes pieminēts','Ēdieni'])
df.plot(x ='Ēdieni', y='Reizes pieminēts', kind = 'bar')
plt.xticks(rotation=0)
plt.show()

mycursor.execute("select nominativs,count(*) from words where grupa = 7 or grupa = 8 group by nominativs order by count(nominativs) desc limit 10")

results = mycursor.fetchall()

Data = {'Reizes pieminēts': [results[0][1],results[1][1],results[2][1],results[3][1],results[4][1],results[5][1],results[6][1],results[7][1],results[8][1],results[9][1]],
        'Dzērieni': [results[0][0],results[1][0],results[2][0],results[3][0],results[4][0],results[5][0],results[6][0],results[7][0],results[8][0],results[9][0]]
       }
  
df = DataFrame(Data,columns=['Reizes pieminēts','Dzērieni'])
df.plot(x ='Dzērieni', y='Reizes pieminēts', kind = 'bar')
plt.xticks(rotation=0)
plt.show()
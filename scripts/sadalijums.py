from pandas import DataFrame
import matplotlib.pyplot as plt
import mysql.connector as mysql

db = mysql.connect(user='root', password='root',host='localhost',database='twitter')
mycursor = db.cursor()
mycursor.execute("select count(*) from media")
results = mycursor.fetchall()
media = results[0][0]

mycursor.execute("select count(*) from vietas")
results = mycursor.fetchall()
places = results[0][0]

mycursor.execute("select COUNT(DISTINCT tvits) from words")
results = mycursor.fetchall()
words = results[0][0]

Data = {'Tvītu skaits miljonos': [media,places,words],
        'Tvītu uzskaitījums': ['Tvīti ar attēlu info','Tvīti ar vietas info', 'Tvīti ar vārdu info']
       }
  
df = DataFrame(Data,columns=['Tvītu skaits miljonos','Tvītu uzskaitījums'])
df.plot(x ='Tvītu uzskaitījums', y='Tvītu skaits miljonos', kind = 'bar')
plt.xticks(rotation=0)
plt.show()

print(media)
print(places)
print(words)
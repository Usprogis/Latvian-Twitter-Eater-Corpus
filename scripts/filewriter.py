x = open("tweetsFinal.json", "w")

x.write("[\n")

read = open(“tweets2011.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2012.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2013Q1.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2013Q2.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2013Q3.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2013Q4.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2014Q1.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2014Q2.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2014Q3.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2014Q4.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2015Q1.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2015Q2.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2016Q1.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2016Q2.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2017.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2018.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2019.json”, “r”)

for line in read:
	x.write(line)
read.close()

read = open(“tweets2020.json”, “r”)

for line in read:
	x.write(line)
read.close()

x.write("]")

x.close()
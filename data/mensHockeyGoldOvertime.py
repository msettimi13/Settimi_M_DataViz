import csv 
import matplotlib.pyplot as plt 

m_1924 = 0
m_1928 = 0
m_1932 = 0
m_1948 = 0
m_1952 = 0
m_1960 = 0
m_1964 = 0
m_1984 = 0
m_1994 = 0
m_1998 = 0
m_2002 = 0
m_2006 = 0
m_2010 = 0
m_2014 = 0


categories = []

with open('mensHockeyGoldOvertime.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0 

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1

		else:
			if (row[0] == "1924") and (row[4] == "CAN"):
				m_1924 += 1
			elif (row[0] == "1928") and (row[4] == "CAN"):
				m_1928 += 1
			elif (row[0] == "1932") and (row[4] == "CAN"):
				m_1932 += 1
			elif (row[0] == "1948") and (row[4] == "CAN"):
				m_1948 += 1
			elif (row[0] == "1952") and (row[4] == "CAN"):
				m_1952 += 1
			elif (row[0] == "1960") and (row[4] == "CAN"):
				m_1960 += 1
			elif (row[0] == "1964") and (row[4] == "CAN"):
				m_1964 += 1
			elif (row[0] == "1984") and (row[4] == "CAN"):
				m_1984 += 1
			elif (row[0] == "1994") and (row[4] == "CAN"):
				m_1994 += 1
			elif (row[0] == "1998") and (row[4] == "CAN"):
				m_1998 += 1
			elif (row[0] == "2002") and (row[4] == "CAN"):
				m_2002 += 1
			elif (row[0] == "2006") and (row[4] == "CAN"):
				m_2006 += 1
			elif (row[0] == "2010") and (row[4] == "CAN"):
				m_2010 += 1
			elif (row[0] == "2014") and (row[4] == "CAN"):
				m_2014 += 1

goldMedalCounts = [m_1924, m_1928, m_1932, m_1948, m_1952, m_1960, m_1964, m_1984, m_1994, m_1998, m_2002, m_2006, m_2010, m_2014]
years = [1924, 1928, 1932, 1948, 1952, 1960, 1964, 1984, 1994, 1998, 2002, 2006, 2010, 2014]

plt.plot(years, goldMedalCounts, color="gold", linewidth=4.0)
plt.xlabel("Olympic Year")
plt.ylabel("Number of Gold Medals")
plt.title("Gold Medals Won by Men in Hockey")
plt.show()
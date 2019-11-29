import csv 
import matplotlib.pyplot as plt 

golds = []
silvers = []
bronzes = []

categories = []

with open('womensMedalsOvertimeCANInfo.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0 

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				golds.append(row[7])
			elif row[7] == "Silver":
				silvers.append(row[7])
			elif row[7] == "Bronze":
				bronzes.append(row[7])

			line_count += 1

print("gold medals: ", len(golds))
print("silver medals: ", len(silvers))
print("bronze medals: ", len(bronzes))

# plot a pie chart
labels = ("Gold", "Silver", "Bronze")
# sizes are how man and how large slices of the pie chart will be 
sizes = [len(golds), len(silvers), len(bronzes)]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0, 0)

plt.pie(sizes, colors=colors, autopct='%1.1f%%')
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medals Won by Women since 1924")
plt.xlabel("Medals since 1924")
plt.show()
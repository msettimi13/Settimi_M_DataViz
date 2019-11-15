import matplotlib.pyplot as plt

hours = [4,8]
activites = ['Sleep', 'Work']
colors - ['r', 'g']

plt.pie(hours, labels=activites, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()
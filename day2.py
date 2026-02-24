import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv")

city_average = data.groupby("city")["score"].mean()


plt.title("Average score by City")
plt.xlabel("City")
plt.ylabel("Average Score")

plt.plot(city_average)
plt.show()
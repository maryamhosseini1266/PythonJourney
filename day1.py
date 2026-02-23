import pandas as pd
import os

data = pd.read_csv("day1/data.csv")
print(data)
print()

print("The Average Score : ",data["score"].mean())
print()

print("The Maximum Score : ",data["score"].max())
print()

print("The Minimum Score : ",data["score"].min())
print()

grouped = data.groupby("city")["score"]

g_mean = grouped.mean()
print("The Average in each city :",g_mean )
print()

g_max = grouped.max()
print("The Maximum score in each city:", g_max)
print()

g_min = grouped.min()
print("The Minimum score in each city:", g_min)
print()
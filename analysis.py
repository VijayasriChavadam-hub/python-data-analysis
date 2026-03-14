import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

print(data.head())
print(data.describe())

plt.scatter(data["sepal_length"], data["petal_length"])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal Length vs Petal Length")
plt.show()

species_count = data["species"].value_counts()
species_count.plot(kind="bar")
plt.title("Distribution of Iris Species")
plt.show()
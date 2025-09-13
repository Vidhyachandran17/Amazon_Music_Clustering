import pandas as pd

# Load clustered data
df = pd.read_csv("clustered_amazon_music.csv")

# Cluster sizes
print("Cluster Sizes:")
print(df["Cluster"].value_counts())

# Average stats per cluster
print("\nCluster Characteristics:")
print(df.groupby("Cluster").mean(numeric_only=True))

# Example: show first 5 rows of each cluster
for c in df["Cluster"].unique():
    print(f"\nSample from Cluster {c}:")
    print(df[df["Cluster"] == c].head())
import matplotlib.pyplot as plt
import seaborn as sns

# Visualize cluster distribution
plt.figure(figsize=(7,5))
sns.countplot(x="Cluster", data=df, palette="viridis")
plt.title("Number of Songs per Cluster")
plt.show()

# Scatterplot of Tempo vs Popularity by Cluster
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="tempo", y="popularity_songs", hue="Cluster", palette="viridis", alpha=0.6)
plt.title("Tempo vs Popularity by Cluster")
plt.show()

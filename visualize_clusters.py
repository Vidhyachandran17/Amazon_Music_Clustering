import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load clustered dataset
df = pd.read_csv("clustered_amazon_music.csv")

# =======================
# 1. Cluster Distribution
# =======================
plt.figure(figsize=(7,5))
sns.countplot(x="Cluster", data=df, palette="viridis")
plt.title("Number of Songs per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Count")
plt.show()

# =======================
# 2. Compare Avg Features
# =======================
features = ["popularity_songs", "duration_ms", "tempo"]
avg_features = df.groupby("Cluster")[features].mean()

print("\n=== Average Features per Cluster ===")
print(avg_features)

# Plot heatmap
plt.figure(figsize=(8,5))
sns.heatmap(avg_features, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Average Features by Cluster")
plt.show()

# =======================
# 3. Scatterplots
# =======================
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="tempo", y="popularity_songs", hue="Cluster", palette="viridis", alpha=0.7)
plt.title("Tempo vs Popularity by Cluster")
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="duration_ms", y="popularity_songs", hue="Cluster", palette="viridis", alpha=0.7)
plt.title("Duration vs Popularity by Cluster")
plt.show()

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv("C:/Users/Vidhya R/Desktop/Amazon_Music_Clustering/data/single_genre_artists.csv")

# Select numeric columns only (important for clustering)
numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
X = data[numeric_cols]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Run KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
data["Cluster"] = kmeans.fit_predict(X_scaled)

# Save with clusters
data.to_csv("C:/Users/Vidhya R/Desktop/Amazon_Music_Clustering/data/songs_with_clusters.csv", index=False)

print("✅ Clustering complete! File saved as songs_with_clusters.csv")

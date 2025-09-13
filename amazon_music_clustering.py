import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the dataset
file_path = r"C:\Users\Vidhya R\Desktop\Amazon_Music_Clustering\data\single_genre_artists.csv"
df = pd.read_csv(file_path)

print("✅ Data loaded successfully!")
print(df.head())

# Select numerical columns for clustering
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
X = df[numeric_cols]

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Save clustered data
output_file = "clustered_amazon_music.csv"
df.to_csv(output_file, index=False)
print(f"✅ Clustered data saved as {output_file}")

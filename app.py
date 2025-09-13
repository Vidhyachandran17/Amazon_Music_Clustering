import streamlit as st
import pandas as pd
import plotly.express as px

# Load clustered data
data_path = r"C:\Users\Vidhya R\Desktop\Amazon_Music_Clustering\clustered_amazon_music.csv"
df = pd.read_csv(data_path)

st.title("🎵 Amazon Music Clustering Dashboard")

# --- Dataset Preview ---
st.subheader("📂 Clustered Songs Data")
st.dataframe(df.head())

# --- Bar Chart: Number of Songs per Cluster ---
st.subheader("📊 Number of Songs per Cluster")
cluster_counts = df['Cluster'].value_counts().sort_index()
fig_bar = px.bar(
    x=cluster_counts.index,
    y=cluster_counts.values,
    labels={"x": "Cluster ID", "y": "Number of Songs"},
    title="Number of Songs in Each Cluster"
)
st.plotly_chart(fig_bar)

# --- Box Plot: Popularity by Cluster ---
st.subheader("⭐ Song Popularity Across Clusters")
if "popularity_songs" in df.columns:
    fig_pop = px.box(
        df,
        x="Cluster",
        y="popularity_songs",
        color="Cluster",
        labels={"Cluster": "Cluster ID", "popularity_songs": "Song Popularity"},
        title="Distribution of Song Popularity per Cluster"
    )
    st.plotly_chart(fig_pop)

# --- Box Plot: Danceability by Cluster ---
st.subheader("💃 Danceability Across Clusters")
if "danceability" in df.columns:
    fig_dance = px.box(
        df,
        x="Cluster",
        y="danceability",
        color="Cluster",
        labels={"Cluster": "Cluster ID", "danceability": "Danceability Score"},
        title="Distribution of Danceability per Cluster"
    )
    st.plotly_chart(fig_dance)

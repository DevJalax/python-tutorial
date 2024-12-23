import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Set your Instagram API credentials
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
access_token = "YOUR_ACCESS_TOKEN"

# Define the API endpoints
liked_posts_endpoint = "https://graph.instagram.com/me/liked_media"
saved_posts_endpoint = "https://graph.instagram.com/me/saved_media"
posted_posts_endpoint = "https://graph.instagram.com/me/media"
story_highlights_endpoint = "https://graph.instagram.com/me/story_highlights"

# Fetch liked posts
response = requests.get(liked_posts_endpoint, params={"access_token": access_token})
liked_posts = response.json()["data"]

# Fetch saved posts
response = requests.get(saved_posts_endpoint, params={"access_token": access_token})
saved_posts = response.json()["data"]

# Fetch posted posts
response = requests.get(posted_posts_endpoint, params={"access_token": access_token})
posted_posts = response.json()["data"]

# Fetch story highlights
response = requests.get(story_highlights_endpoint, params={"access_token": access_token})
story_highlights = response.json()["data"]

# Create a Pandas dataframe to store the collected data
df = pd.DataFrame({
    "liked_posts": liked_posts,
    "saved_posts": saved_posts,
    "posted_posts": posted_posts,
    "story_highlights": story_highlights
})

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer()
vectorized_data = vectorizer.fit_transform(df["liked_posts"] + df["saved_posts"] + df["posted_posts"] + df["story_highlights"])

# Apply K-Means clustering to identify patterns and characteristics
kmeans = KMeans(n_clusters=5)
kmeans.fit(vectorized_data)

# Create a digital twin representation based on the clustering results
digital_twin = kmeans.cluster_centers_

# **Holographic Visualization**
def visualize_hologram(digital_twin):
    # Create a 3D scatter plot of the digital twin representation
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Generate random colors for each cluster center for visualization purposes
    colors = np.random.rand(len(digital_twin), 3)

    # Plot each cluster center in 3D space
    ax.scatter(digital_twin[:, 0], digital_twin[:, 1], digital_twin[:, 2], c=colors, s=100)

    ax.set_title('Digital Twin Holographic Representation')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Feature 3')

    plt.show()

# Call the visualization function with the digital twin data
visualize_hologram(digital_twin)

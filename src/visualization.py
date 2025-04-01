# src/visualization.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def plot_film_ratings(films):
   
    df = pd.DataFrame(films)

    if "Metascore" not in df.columns or "title" not in df.columns:
        raise ValueError("Les colonnes nécessaires pour la visualisation sont absentes.")
    
    # Graphique avec Seaborn
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x="title", y="Metascore", palette="viridis")
    plt.xticks(rotation=45)
    plt.title("Notes Metascore des films")
    
    st.pyplot(plt)
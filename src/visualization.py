# src/visualization.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st  # Import Streamlit pour afficher les graphiques

def plot_film_ratings(films):
    # Convertir les films en DataFrame
    df = pd.DataFrame(films)
    
    # Vérifier que les colonnes nécessaires sont présentes
    if "Metascore" not in df.columns or "title" not in df.columns:
        raise ValueError("Les colonnes nécessaires pour la visualisation sont absentes.")
    
    # Créer le graphique avec Seaborn
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x="title", y="Metascore", palette="viridis")
    plt.xticks(rotation=45)
    plt.title("Notes Metascore des films")
    
    # Utiliser Streamlit pour afficher le graphique
    st.pyplot(plt)

# src/app.py

import streamlit as st
from queries_mongodb import get_films, insert_film, update_film, delete_film
from queries_neo4j import create_node, find_shortest_path
from visualization import plot_film_ratings

st.title("Application MongoDB et Neo4j")

# Section MongoDB - Films
st.header("Films dans MongoDB")
films = get_films(limit=10)  # Limite à 10 films

if len(films) == 0:
    st.write("Aucun film trouvé.")
else:
    st.write("Liste des films :")
    for film in films:
        try:
            st.write(f"{film['title']} - Note Metascore: {film.get('Metascore', 'N/A')}")
        except KeyError:
            st.error("Erreur affichage film")

# Visualisation des notes IMDb des films (si disponibles)
if st.button("Visualiser les notes IMDb"):
    plot_film_ratings(films)

# Section Neo4j - Graphe des relations entre films/personnages/etc.
st.header("Neo4j")
node1 = st.text_input("Nom du premier nœud")
node2 = st.text_input("Nom du second nœud")

if st.button("Trouver le chemin le plus court"):
    path = find_shortest_path(node1, node2)
    if path:
        st.write("Chemin trouvé :")
        st.write(path)
    else:
        st.write("Aucun chemin trouvé.")

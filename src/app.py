# src/app.py

import streamlit as st
from queries_mongodb import get_films, insert_film, update_film, delete_film
from queries_neo4j import create_node, find_shortest_path
from visualization import *
from crud import *

st.title("Projet : Exploration et Interrogation de Bases de Données NoSQL avec Python")

st.header("Films dans MongoDB (limite à 10 films)")
films = get_films(limit=10)  # Limite à 10 films

if len(films) == 0:
    st.write("Aucun film trouvé.")
else:
    for film in films:
        try:
            st.write(f"ID: {film['_id']} | {film['title']} - Note Metascore: {film.get('Metascore', 'N/A')}")
        except KeyError:
            st.error("Erreur affichage film")

# Notes Metascore des films 
if st.button("Visualiser les notes Metascore"):
    plot_film_ratings(films)

# Partie CRUD (Create, Read, Update, Delete)
st.header("CRUD (Create, Read, Update, Delete)")

# Ajouter un film
if st.button("Ajouter un film"):
    insert_film_form()

# Mettre à jour un film
st.subheader("Mettre à jour un film")
film_id_to_update = st.text_input("ID du film à mettre à jour")
new_title = st.text_input("Nouveau titre du film", value="Nouveau titre")
if st.button("Mettre à jour le titre"):
    update_film_form(film_id_to_update, new_title)

# Supprimer un film
st.subheader("Supprimer un film")
film_id_to_delete = st.text_input("ID du film à supprimer")
if st.button("Supprimer le film"):
    delete_film_form(film_id_to_delete)

# Section Neo4j
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

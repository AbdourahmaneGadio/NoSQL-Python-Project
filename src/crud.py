import streamlit as st
from queries_mongodb import get_films, insert_film, update_film, delete_film

def insert_film_form():
    with st.form(key="insert_form"):
            title = st.text_input("Titre")
            genre = st.text_input("Genre")
            description = st.text_area("Description")
            director = st.text_input("Réalisateur")
            actors = st.text_input("Acteurs (séparés par des virgules)")
            year = st.number_input("Année", min_value=1900, max_value=2100, step=1)
            runtime = st.number_input("Durée (en minutes)", min_value=1)
            rating = st.selectbox("Classification", ["G", "PG", "PG-13", "R", "NC-17"])
            votes = st.number_input("Nombre de votes", min_value=0)
            revenue = st.number_input("Revenu (en millions)", min_value=0.0)
            metascore = st.number_input("Metascore", min_value=0, max_value=100)

            submit_button = st.form_submit_button(label="Ajouter le film")

            if submit_button:
                new_film = {
                    "title": title,
                    "genre": genre,
                    "Description": description,
                    "Director": director,
                    "Actors": actors,
                    "year": year,
                    "Runtime (Minutes)": runtime,
                    "rating": rating,
                    "Votes": votes,
                    "Revenue (Millions)": revenue,
                    "Metascore": metascore,
                }
                if insert_film(new_film):
                    st.success(f"Film '{title}' ajouté avec succès !")
                else:
                    st.error(f"Erreur lors de l'ajout du film '{title}'.")


def update_film_form(film_id_to_update, new_title):
    if update_film(film_id_to_update, {"title": new_title}):
        st.success(f"Film avec ID {film_id_to_update} mis à jour.")
    else:
        st.error(f"Erreur lors de la mise à jour du film avec ID {film_id_to_update}.")

def delete_film_form(film_id_to_delete):
    if delete_film(film_id_to_delete):
        st.success(f"Film avec ID {film_id_to_delete} supprimé.")
    else:
        st.error(f"Erreur lors de la suppression du film avec ID {film_id_to_delete}.")

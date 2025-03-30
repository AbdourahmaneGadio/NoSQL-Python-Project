import streamlit as st
import pymongo # Pour se connecter a MongoDb

# Connexion a la base de donnees (https://docs.streamlit.io/develop/tutorials/databases/mongodb)

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    try:
        return pymongo.MongoClient(**st.secrets["mongo"])
    except Exception as e:
        st.error(f"Erreur de connexion à MongoDB : {e}")
        return None

client = init_connection()

if not client:
    st.error("Echec connexion")
else:
    #st.write("Connexion OK")

    # Pull data from the collection.
    # Uses st.cache_data to only rerun when the query changes or after 10 min.
    @st.cache_data(ttl=600)
    def get_data():
        try:
            db = client.entertainment # base de donnees entertainment
            films = db.films.find() # La collection films
            films = list(films)  # make hashable for st.cache_data
            return films
        except Exception as e:
            st.error(f"Erreur lors de la récupération des données : {e}")
            return []

    films = get_data()

    if len(films) == 0:
        st.write(f"Base de donnees vide...")
    else:
        # Print results.
        st.write(f"Films disponibles :")
        for film in films:
            try:
                st.write(f"Id {film["_id"]} : {film["title"]}")
            except:
                st.error(f"Probleme affichage du film")

        # Interrogation de MongoDB

        # Interrogation de Neo4j

        # Analyse et Visualisation

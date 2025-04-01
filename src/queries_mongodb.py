
from database import init_mongo_connection
import streamlit as st

# Initialisation de la connexion MongoDB
clientMongoDB = init_mongo_connection()

if not clientMongoDB:
    st.error(f"Erreur lors de la connexion MongoDB : {e}")
else:
    st.success(f"Connexion MongoDB OK")

# Recupere les films
def get_films(limit=10):
    try:
        db = clientMongoDB.entertainment  # Base de données "entertainment"
        films = db.films.find().limit(limit)  # Collection "films", limite de documents
        return list(films)  
    except Exception as e:
        raise Exception(f"Erreur lors de la récupération des films : {e}")

# Insere un film
def insert_film(film):
    try:
        db = clientMongoDB.entertainment
        result = db.films.insert_one(film)  
        return result.inserted_id  
    except Exception as e:
        raise Exception(f"Erreur lors de l'insertion du film : {e}")

# Met a jour un film
def update_film(film_id, updates):
    try:
        db = clientMongoDB.entertainment
        result = db.films.update_one({"_id": film_id}, {"$set": updates}) 
        return result.modified_count  
    except Exception as e:
        raise Exception(f"Erreur lors de la mise à jour du film : {e}")

# Supprime un film
def delete_film(film_id):
    try:
        db = clientMongoDB.entertainment
        result = db.films.delete_one({"_id": film_id})  
        return result.deleted_count  
    except Exception as e:
        raise Exception(f"Erreur lors de la suppression du film : {e}")

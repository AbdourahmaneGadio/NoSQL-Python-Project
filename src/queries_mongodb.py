# src/queries_mongodb.py

from database import init_mongo_connection
import streamlit as st

# Initialisation de la connexion MongoDB
clientMongoDB = init_mongo_connection()

if not clientMongoDB:
    st.error(f"Erreur lors de la connexion MongoDB : {e}")
else:
    st.success(f"Connexion MongoDB OK")

def get_films(limit=10):
    try:
        db = clientMongoDB.entertainment  # Base de données "entertainment"
        films = db.films.find().limit(limit)  # Collection "films", limite de documents
        return list(films)  # Convertir en liste
    except Exception as e:
        raise Exception(f"Erreur lors de la récupération des films : {e}")

def insert_film(film):
    try:
        db = clientMongoDB.entertainment
        result = db.films.insert_one(film)  # Insérer un document dans la collection "films"
        return result.inserted_id  # Retourner l'ID du document inséré
    except Exception as e:
        raise Exception(f"Erreur lors de l'insertion du film : {e}")

def update_film(film_id, updates):
    try:
        db = clientMongoDB.entertainment
        result = db.films.update_one({"_id": film_id}, {"$set": updates})  # Mettre à jour le document correspondant
        return result.modified_count  # Retourner le nombre de documents modifiés
    except Exception as e:
        raise Exception(f"Erreur lors de la mise à jour du film : {e}")

def delete_film(film_id):
    try:
        db = clientMongoDB.entertainment
        result = db.films.delete_one({"_id": film_id})  # Supprimer le document correspondant
        return result.deleted_count  # Retourner le nombre de documents supprimés
    except Exception as e:
        raise Exception(f"Erreur lors de la suppression du film : {e}")

# src/queries_mongodb.py

from database import init_mongo_connection

clientMongoDB = init_mongo_connection()

def get_films(limit=10):
    """
    Récupère une liste de films depuis MongoDB avec une limite.
    """
    try:
        db = clientMongoDB.entertainment  # Base de données "entertainment"
        films = db.films.find().limit(limit)  # Collection "films", limite de 10 documents
        return list(films)  # Convertir en liste
    except Exception as e:
        raise Exception(f"Erreur lors de la récupération des films : {e}")

def insert_film(film):
    """
    Insère un nouveau film dans MongoDB.
    """
    try:
        db = clientMongoDB.entertainment
        result = db.films.insert_one(film)
        return result.inserted_id
    except Exception as e:
        raise Exception(f"Erreur lors de l'insertion du film : {e}")

def update_film(film_id, updates):
    """
    Met à jour un film existant dans MongoDB.
    """
    try:
        db = clientMongoDB.entertainment
        result = db.films.update_one({"_id": film_id}, {"$set": updates})
        return result.modified_count
    except Exception as e:
        raise Exception(f"Erreur lors de la mise à jour du film : {e}")

def delete_film(film_id):
    """
    Supprime un film de MongoDB.
    """
    try:
        db = clientMongoDB.entertainment
        result = db.films.delete_one({"_id": film_id})
        return result.deleted_count
    except Exception as e:
        raise Exception(f"Erreur lors de la suppression du film : {e}")

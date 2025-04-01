import pymongo
from neo4j import GraphDatabase
from config import get_mongo_secrets, get_neo4j_secrets
import streamlit as st

# Se connecte a la base MongoDB
@st.cache_resource
def init_mongo_connection():
    try:
        mongo_secrets = get_mongo_secrets()
        return pymongo.MongoClient(mongo_secrets["host"])
    except Exception as e:
        st.error(f"Erreur de connexion à MongoDB : {e}")
        return None

# Se connecte a la base Neo4J
@st.cache_resource
def init_neo4j_connection():
    try:
        neo4j_secrets = get_neo4j_secrets()
        return GraphDatabase.driver(
            neo4j_secrets["uri"],
            auth=(neo4j_secrets["user"], neo4j_secrets["password"])
        )
    except Exception as e:
        st.error(f"Erreur de connexion à Neo4j : {e}")
        return None

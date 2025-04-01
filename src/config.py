import streamlit as st

# Les variables d'environnement de MongoDB
def get_mongo_secrets():
    try:
        return st.secrets["mongo"]
    except KeyError:
        raise Exception("Les secrets MongoDB ne sont pas configurés correctement.")

# Les variables d'environnement de Neo4J
def get_neo4j_secrets():
    try:
        return st.secrets["neo4j"]
    except KeyError:
        raise Exception("Les secrets Neo4j ne sont pas configurés correctement.")

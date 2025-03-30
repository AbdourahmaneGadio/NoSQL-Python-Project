# src/config.py

import streamlit as st

def get_mongo_secrets():
    try:
        return st.secrets["mongo"]
    except KeyError:
        raise Exception("Les secrets MongoDB ne sont pas configurés correctement.")

def get_neo4j_secrets():
    try:
        return st.secrets["neo4j"]
    except KeyError:
        raise Exception("Les secrets Neo4j ne sont pas configurés correctement.")

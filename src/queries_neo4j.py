# src/queries_neo4j.py

from database import init_neo4j_connection

driverNeo4j = init_neo4j_connection()

def create_node(label, properties):
    query = f"CREATE (n:{label} $props) RETURN n"
    with driverNeo4j.session() as session:
        result = session.run(query, props=properties)
        return [record["n"] for record in result]

def find_shortest_path(node1, node2):
    query = """
    MATCH (a)-[*]-(b)
    WHERE a.name = $node1 AND b.name = $node2
    RETURN shortestPath((a)-[*]-(b)) AS path
    """
    with driverNeo4j.session() as session:
        result = session.run(query, node1=node1, node2=node2)
        return [record["path"] for record in result]

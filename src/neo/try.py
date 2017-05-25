from neo4j.v1 import GraphDatabase

uri = "bolt://203.246.82.121:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "900416"))

def print_friends_of(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a:Person)-[]->(f:Store) "
                                 "RETURN f.name"):
                print(record["f.name"])

print_friends_of("김민석")

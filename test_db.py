import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="avalon_research",
    user="postgres",
    password="divergent13@A"
)
print("Connected successfully")
conn.close()
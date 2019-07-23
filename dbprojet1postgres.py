import psycopg2
con=psycopg2.connect (
    host= "localhost",
    database="projet1",
    user="postgres",
    password="ngagne03",
    port ="5432"
)
#connection = psycopg2.connect(con)
cur=con.cursor()
#create table into prosenegal Database

cur.execute(
"""CREATE TABLE region (
            id_reg SERIAL PRIMARY KEY,
            nom_reg VARCHAR(255) NOT NULL
)
""")

cur.execute("""CREATE TABLE departement (
            id_dep SERIAL PRIMARY KEY,
            nom_dep VARCHAR(255) NOT NULL,
            id_reg INTEGER ,
            FOREIGN KEY (id_reg)
            REFERENCES region (id_reg)
            ON UPDATE CASCADE ON DELETE CASCADE
)
""")

cur.execute("""CREATE TABLE commune (
            id_com SERIAL PRIMARY KEY,
            nom_com VARCHAR(255) NOT NULL,
            id_dep INTEGER,
            FOREIGN KEY (id_dep)
            REFERENCES departement (id_dep)
            ON UPDATE CASCADE ON DELETE CASCADE
        
)
""")


cur.execute("""CREATE TABLE arrondissement (
            id_ar SERIAL PRIMARY KEY,
            nom_ar VARCHAR(255) NOT NULL,
            ta FLOAT8,
            mo FLOAT8,
            se FLOAT8,
            id_com INTEGER,
            FOREIGN KEY (id_com)
            REFERENCES commune (id_com)
            ON UPDATE CASCADE ON DELETE CASCADE
            
)
""")
con.commit()
cur.close()



        


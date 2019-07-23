import psycopg2
con=psycopg2.connect (
    host= "localhost",
    database="sonatel7",
    user="postgres",
    password="ngagne03",
    port ="5432"
)
#connection = psycopg2.connect(con)
cur=con.cursor()
#create table into sonatel1 from postgres Database

cur.execute(
"""CREATE TABLE referentiel (
            id_ref SERIAL PRIMARY KEY,
            nom_ref VARCHAR(255) NOT NULL
)
""")

cur.execute(
"""CREATE TABLE promotion (
            id_promo SERIAL PRIMARY KEY,
            nom_promo VARCHAR(255) NOT NULL,
            date_deb DATE,
            date_fin DATE,
            id_ref INTEGER,
            FOREIGN KEY (id_ref)
            REFERENCES referentiel (id_ref)
            

)
""")

cur.execute(
"""CREATE TABLE Apprenant2 (
            id_ap SERIAL PRIMARY KEY,
            matricule VARCHAR(255),
            pseudo VARCHAR(255) NOT NULL,
            nom_ap VARCHAR(255) NOT NULL,
            prenom_ap VARCHAR(255) NOT NULL,
            date_nais DATE NOT NULL,
            statu VARCHAR(255) NOT NULL,
            sexe_ap VARCHAR(255) NOT NULL,
            id_promo INTEGER,
            FOREIGN KEY (id_promo)
            REFERENCES promotion (id_promo)
           
            
            
)
""")

con.commit()
cur.close()



        


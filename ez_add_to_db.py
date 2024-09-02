import mysql.connector
import os

db = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database=os.environ.get("DB_NAME")
      )
    
while True:   
    print("Connexion à la base de donnée réussie")
    print("----------------------")
    print("choisissez une option")
    print("1 - Ajouter un groupe")
    print("2 - Ajouter une formation")
    print("----------------------")
    option = input("Votre choix : ")

    if option == "1":
        # choix de la formation où ajouter le groupe
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `uppa_formation`;")
        result = cursor.fetchall()
        print("Liste des formations : ")
        for i in result:
            print(f"{i[0]} - {i[1]}")
        formation_id = input("ID de la formation où ajouter le groupe : ")
        nom = input("Nom du groupe : ")
        ics_link = input("Lien ics du groupe : ")
        
        cursor.execute("INSERT INTO `uppa_groupe` (`nom`, `lien_ics`) VALUES (%s, %s);", (nom, ics_link))
        cursor.execute("SELECT LAST_INSERT_ID();")
        groupe_id = cursor.fetchone()[0]
        
        cursor.execute("INSERT INTO `uppa_rel_formation_groupe` (`formation_id`, `groupe_id`) VALUES (%s, %s);", (formation_id, groupe_id))
        db.commit()
        cursor.close()
        print("Groupe ajouté avec succès")
    
    if option == "2":
        nom = input("Nom de la formation : ")
        description = input("Description de la formation : ")
        lieux = input("Lieux de la formation : ")
        cursor = db.cursor()
        cursor.execute("INSERT INTO `uppa_formation` (`nom`, `description`, `lieux`) VALUES (%s, %s, %s);", (nom, description, lieux))
        db.commit()
        cursor.close()
        print("Formation ajoutée avec succès")
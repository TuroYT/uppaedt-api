import mysql.connector
import os

db = mysql.connector.connect(
  host=os.environ.get("DB_HOST"),
  user=os.environ.get("DB_USER"),
  password=os.environ.get("DB_PASS")
)


# Class principale
class BDD:
  def __init__(self) -> None:
    
    try:
      self.__db = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database=os.environ.get("DB_NAME")
      )
    except Exception as e:
      print(f"Erreur : {e}")
      
      
  def get_all_formations(self):
    """Recupère la liste des Formations de l'uppa

    Returns:
        dict: clefs = id, nom, description, lieux
    """

    cursor = self.__db.cursor()
    cursor.execute("SELECT * FROM `uppa_formation`;")
    result = cursor.fetchall()
    
    to_return = {
      "id":result[0],
      "nom":result[1],
      "description":result[2],
      "lieux":result[3]
    }
    
    cursor.close()

    return to_return


print(BDD().get_all_formations())
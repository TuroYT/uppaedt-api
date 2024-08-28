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
        dict[]: clefs = id, nom, description, lieux
    """

    cursor = self.__db.cursor()
    cursor.execute("SELECT * FROM `uppa_formation`;")
    result = cursor.fetchall()
    
    res = []
    for i in result:
      res.append({
        "id":i[0],
        "nom":i[1],
        "description":i[2],
        "lieux":i[3]
      })

    
    cursor.close()
    return res
  
  def get_all_groupe(self):
    """get all groupes

    Returns:
        dict[]: key = id, nom, ics_link
    """
    
    cursor = self.__db.cursor()
    cursor.execute("SELECT * FROM `uppa_groupe`;")
    result = cursor.fetchall()
    to_return = []
    for i in result:
      to_return.append({
        "id":i[0],
        "nom":i[1],
        "ics_link":i[2]
      })
    
    cursor.close()
    return to_return
    
  def get_ic_link(self, id):
    """get ics link from id

    Args:
        id (int): id du groupe

    Returns:
        str: lien ics ou None
    """
    cursor = self.__db.cursor()
    cursor.execute(f"SELECT ics_link FROM `uppa_groupe` WHERE id = {id};")
    result = cursor.fetchall()
    cursor.close()
    return result[0][0]

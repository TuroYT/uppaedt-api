import time
import icalendar
from pytz import timezone
import requests
import os
import json

def ics_to_json(file_path):
    # Définir le fuseau horaire de Paris
    paris_tz = timezone('Europe/Paris')

    # Ouvrir le fichier .ics
    with open(file_path, 'rb') as f:
        cal = icalendar.Calendar.from_ical(f.read())

    events = []

    # Parcourir tous les événements dans le calendrier
    for component in cal.walk():
        if component.name == "VEVENT":
            # Convertir les dates en heure de Paris
            start = component.get('dtstart').dt.astimezone(paris_tz)
            end = component.get('dtend').dt.astimezone(paris_tz)

            description = str(component.get('description')).split("\n")

            if len(description) == 6:
                cours = description[2]
                prof = description[3]
            else:
                cours = description[2]
                prof = "NA"
                
            
            event = {
                "summary": str(component.get('summary')),
                "description" : cours,
                "prof": prof,
                "start": str(start),
                "end": str(end),
                "location": str(component.get('location')),
                "uid": str(component.get('uid'))
            }
            events.append(event)


    # Trier les événements par date de début
    events.sort(key=lambda x: x['start'])

    return events




def get_json_from_icsLink(ics_link, groupname):
    print(f"Le groupe {groupname} a été demandé")
    try :
        if os.path.exists(groupname) and (os.path.getmtime(groupname) > time.time() - 86400):
            return json.loads(open(groupname).read())
        else:
            data = requests.get(ics_link).content
            open("tmp","wb").write(data)
            res = ics_to_json("tmp")
            os.remove("tmp")
            open(f"{groupname}","w").write(json.dumps(res))
            return res
    except :
        data = requests.get(ics_link).content
        open("tmp","wb").write(data)
        res = ics_to_json("tmp")
        os.remove("tmp")
        print("Une erreur est survenue")
        return res
    
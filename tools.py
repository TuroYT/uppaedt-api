import time
import icalendar
from pytz import timezone
import requests
import os
import json
from datetime import datetime, timedelta


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
            start = component.get('dtstart').dt
            end = component.get('dtend').dt

            # Check if start and end are date objects and convert them to datetime
            if isinstance(start, datetime) is False:
                start = datetime.combine(start, datetime.min.time())
            if isinstance(end, datetime) is False:
                end = datetime.combine(end, datetime.min.time())

            start = start.astimezone(paris_tz)
            end = end.astimezone(paris_tz)

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




def get_json_from_icsLink(ics_link, groupname=None):
    '''
    Cette fonction prend en paramètre un lien ics et retourne un json contenant les événements du calendrier
    '''
    if groupname is None:
        print("lien ics demandé : ", ics_link)
    else:
        print(f"Le groupe {groupname} a été demandé")
    try :
        data = requests.get(ics_link, verify=False).content
        open("tmp","wb").write(data)
        res = ics_to_json("tmp")
        os.remove("tmp")
        return res
    except Exception as e:
        print("Une erreur est survenue")
        return {"error": f"Une erreur est survenue {e}"}
    
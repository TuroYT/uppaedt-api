import icalendar
from pytz import timezone
import requests
import os
from datetime import datetime, timedelta


def ics_to_json(file_path, type):
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
            if type == 0:
                if len(description) == 6:
                    cours = description[2]
                    prof = description[3]
                else:
                    cours = description[2]
                    prof = "NA"
            elif type == 1:
                if len(description) == 1:
                    cours = ""
                    prof = ""
                else:
                    print(description)
                    cours = description[0]
                    prof = description[1]
            
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




def get_json_from_icsLink(ics_link, type=0):
    '''
    Cette fonction prend en paramètre un lien ics et retourne un json contenant les événements du calendrier
    
    type : 0 -> planning Générique
    type : 1 -> Hyperplanning
    '''
    
    
    
    try :
        data = requests.get(ics_link, verify=False).content
        open("tmp","wb").write(data)
        res = ics_to_json("tmp", type)
        print(res)
        os.remove("tmp")
        return res
    except Exception as e:
        print("Une erreur est survenue")
        return {"error": f"Une erreur est survenue {e}"}
    
#print(get_json_from_icsLink("https://univ-pau-planning2024-25.hyperplanning.fr/hp/Telechargements/ical/Edt_L1_LLCER___EA.ics?version=2024.0.8.0&icalsecurise=5325F56562BE3FC2802FB022452E2B39DBD97A98D5DE32A67275D56B03D3D0D7F82E9676C6048CB0BD98298EA97C99C1&param=643d5b312e2e36325d2666683d3126663d3131303030", 1))

# {'summary': 'TD B - Civilisation S1 - MCNAMEE - TD', 'description': 'Enseignant : MCNAMEE', 'prof': 'Type : TD', 'start': '2024-12-03 14:30:00+01:00', 'end': '2024-12-03 16:00:00+01:00', 'location': '30 Salle de cours', 'uid': 'Cours-33037-15-L1_LLCER_-_EA-Index-Education'}
API_VERSION = "1.2.0"

from fastapi import FastAPI, HTTPException
from tools import get_json_from_icsLink
from fastapi.middleware.cors import CORSMiddleware
from database import BDD
from logger import Logger

Logger = Logger()
app = FastAPI()



group_links = {
    "but1_g1": "https://ade.univ-pau.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=4962,4989&projectId=6&calType=ical&nbWeeks=99",
    "but1_g2": "https://ade.univ-pau.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=4963,4990&projectId=6&calType=ical&nbWeeks=99",
    "but1_g3": "https://ade.univ-pau.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=4964,4991&projectId=6&calType=ical&nbWeeks=99",
    "but1_g4": "https://ade.univ-pau.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=4965,4992&projectId=6&calType=ical&nbWeeks=99",

    "s4_cyber": "https://ade.univ-pau.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=4975&projectId=6&calType=ical&nbWeeks=99",
    "s4_rom" : "https://ade.univ-pau.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=26709&projectId=6&calType=ical&nbWeeks=99", 
    "s4_pilpro" : "https://ade.univ-pau.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=4987&projectId=6&calType=ical&nbWeeks=99",
}

app = FastAPI()


@app.get("/")
def read_root():
    return {"VERSION" : API_VERSION}

@app.get("/api/planning/getPlanningPerName/{groupname}")
def read_root(groupname : str):
    return get_json_from_icsLink(group_links[groupname], groupname)


@app.post("/api/planning/getPlanningPerLink/}")
def read_root(link : str):
    return get_json_from_icsLink(link)

@app.post("/api/planning/getPlanningPerId/")
def read_root(id: int):
    try:
        return get_json_from_icsLink(BDD().get_ics_link(id))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/formations/getall")
def read_root():
    try:
        return BDD().get_all_formations()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/groupes/getallwithformations")
def read_root():
    try:
        res = []
        formations = BDD().get_all_formations()
        for formation in formations:
            groupes = BDD().get_groups_from_formation(formation["id"])
            if len(groupes) > 0 :
                res.append({
                    "formation": formation,
                    "groupes": BDD().get_groups_from_formation(formation["id"])
                })
        print(res)
        return res
    
    
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/groupes/getFromFormation")
def read_root( formation_id: int):
    try:
        return BDD().get_groups_from_formation(formation_id=formation_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/api/groupes/getFromId/{id}")
def read_root( id: int):
    try:
        groups = BDD().get_all_groupe()
        for group in groups:
            if group["id"] == id:
                return group
        return []
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
        

    
    
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
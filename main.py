API_VERSION = "1.1.1"


from fastapi import FastAPI, Response
from tools import get_json_from_icsLink
from fastapi.middleware.cors import CORSMiddleware
from database import BDD
from logger import Logger

Logger = Logger()
BDD = BDD()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
def read_root(response:Response):
    response.headers["Access-Control-Allow-Origin"] = '*'
    Logger.info("Main Acceded")
    return {"VERSION" : API_VERSION}

@app.get("/api/planning/getPlanningPerName/{groupname}")
def read_root(groupname : str, response:Response):
    response.headers["Access-Control-Allow-Origin"] = '*'
    return get_json_from_icsLink(group_links[groupname], groupname)


@app.post("/api/planning/getPlanningPerLink/}")
def read_root(link : str, response:Response):
    response.headers["Access-Control-Allow-Origin"] = '*'
    return get_json_from_icsLink(link)

@app.post("/api/planning/getPlanningPerId/")
def read_root(id : int, response:Response):
    response.headers["Access-Control-Allow-Origin"] = '*'
    return get_json_from_icsLink(BDD.get_ics_link(id))


@app.get("/api/formations/getall")
def read_root(response:Response):
    response.headers["Access-Control-Allow-Origin"] = '*'
    return BDD.get_all_formations()

@app.get("/api/groupes/getall")
def read_root(response:Response):
    response.headers["Access-Control-Allow-Origin"] = '*'
    return BDD.get_all_groupe()


@app.get("/api/groupes/get_from_formationid")
def read_root(response:Response, formation_id: int):
    response.headers["Access-Control-Allow-Origin"] = '*'
    return BDD.get_groups_from_formation(formation_id=formation_id)
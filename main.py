from fastapi import FastAPI, Response
from tools import get_json_from_icsLink
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/api/planning/getPlanningPerName/{groupname}")
def read_root(groupname : str, response:Response):
    response.headers["Access-Control-Allow-Origin"] = '*'
    return get_json_from_icsLink(group_links[groupname], groupname)






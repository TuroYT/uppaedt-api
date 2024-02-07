from fastapi import FastAPI
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
    "but1_g1": "",
    "but1_g2": "",
    "but1_g3": "https://ade.univ-pau.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=4964,4991&projectId=6&calType=ical&nbWeeks=99",
    "but1_g4": ""
    
}

app = FastAPI()


@app.get("/api/planning/getPlanningPerName/{groupname}")
def read_root(groupname : str ):
    return get_json_from_icsLink(group_links[groupname])







# Edt4rt API

API interne pour récuperer les cours sur ade.univ-pau.fr




## API Reference

#### Get all events

```http
  GET /api/planning/getPlanningPerName/{groupname}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `groupname` | `string` | **Required**. return a list of event |

it can be but1_g1, but1_g2, but1_g3, but1_g4



## Run Locally

Start the server

```bash
  uvicorn main:app --reload
```


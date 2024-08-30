
# Edt4rt API

API interne pour récuperer les cours sur ade.univ-pau.fr




## documentation

```http
  GET /docs
```




## Run Locally

Start the server

```bash
  uvicorn main:app --reload
```


## Run via docker

Start the server

```bash
  docker run -d -p 9999:9999 --restart always turodev/edt4rt-api
```

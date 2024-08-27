
## Table : `uppa_formation

| Colonne     | Type de données | 
|-------------|-----------------|-
| `id`        | INTEGER         | 
| `nom`       | TEXT            | 
| `description` | TEXT            |
| `lieux`     | TEXT            | 


## Table : `uppa_groupe

| Colonne     | Type de données | 
|-------------|-----------------|-
| `id`        | INTEGER         | 
| `nom`       | TEXT            | 
| `lien_ics`     | TEXT            | 

## Table : `uppa_rel_formation_groupe

| Colonne     | Type de données | 
|-------------|-----------------|-
| `formation_id`        | INTEGER         | 
| `groupe_id`       | INTEGER            | 
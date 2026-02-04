# Prosjektbeskrivelse – IT-utviklingsprosjekt (2IMI)

##  game saves
**game saves**

---

## Deltakere
- sebastian – backend/database
- oskar – game programer
 

---

## 1. Prosjektidé og problemstilling

### Beskrivelse
vi lager et spill der progresjonen din blir lagret i en db


### Målgruppe
er laget for de som har lyst til og spille et lite spill og ha det gåy mer enn en gang

---

## 2. Funksjonelle krav

Systemet skal minst ha følgende funksjoner:

1. Funksjon 1  
2. Funksjon 2  
3. Funksjon 3  
4. Funksjon 4  
5. Funksjon 5  

*(Legg til flere hvis nødvendig)*

---

## 3. Teknologivalg

### Programmeringsspråk
- Eksempel: Python / JavaScript 

### Rammeverk / Plattform / Spillmotor
- Eksempel: Flask 

### Database
- MariaDB

### Verktøy
- GitHub
- GitHub Projects (Kanban)
- Eventuelle andre verktøy

---

## 4. Datamodell

### Oversikt over tabeller

**Tabell 1:**
- Navn: *users*
- Beskrivelse:*holder info om alle brukere*

**Tabell 2:**
- Navn: *runs*
- Beskrivelse: *holder info om hver spill som har blitt startet*

*(Minst 2–4 tabeller)*

### Eksempel på tabellstruktur


**users:**

``` sql
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int(11)      | NO   | PRI | NULL    | auto_increment |
| name  | varchar(255) | NO   |     | NULL    |                |
| email | varchar(255) | NO   |     | NULL    |                |
| pword | varchar(255) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+

```



**runs:**
```sql
+---------+------------+------+-----+---------+----------------+
| Field   | Type       | Null | Key | Default | Extra          |
+---------+------------+------+-----+---------+----------------+
| id      | int(11)    | NO   | PRI | NULL    | auto_increment |
| hp      | int(11)    | NO   |     | NULL    |                |
| e_hp    | int(11)    | NO   |     | NULL    |                |
| user_id | int(11)    | YES  | MUL | NULL    |                |
| done    | tinyint(1) | YES  |     | 0       |                |
+---------+------------+------+-----+---------+----------------+
```